from __future__ import absolute_import

import argparse
import six
import sys
import uuid
import pandas as pd
import numpy as np
from datetime import date

import logging
logging.basicConfig(filename = "monitoring.log", level = logging.INFO)

from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException

_DEFAULT_LOCATION_IDS = '2840' # United States
_DEFAULT_LANGUAGE, _DEFAULT_LANGUAGE_ID = 'english', '1000'
_DEFAULT_LIMIT = 1000
today = str(date.today())
search_network = 'GOOGLE_SEARCH_AND_PARTNERS'
F_interval = 'NEXT_QUARTER'

def main(client, customer_id, location_ids, language_id, keywords, page_urls, limit):
    if not (keywords or page_urls):
        logging.info('No seed input')
        sys.exit(1)

    if keywords and page_urls:
        logging.info('Specify one input type only')
        sys.exit(1)
    
    # generate ideas DataFrame with loop
    if keywords:
        for location_id in location_ids:
            for keyword in keywords:
                keyword = [keyword]
                # the input keyword for create_ideas must be of list format
                tmp = create_ideas(client, customer_id, location_id, language_id, keyword, page_urls, limit)
                # generate a plan with historic and forecasting metrics if the dataframe exists
                if tmp.empty:
                    title_frame = 'null_result_{}.csv'.format(uuid.uuid4())
                    tmp.to_csv(title_frame, index = False)
                else:
                    plan_metrics(client, customer_id, location_id, tmp)
    
    else:
        for location_id in location_ids:
            for page_url in page_urls:
                tmp = create_ideas(client, customer_id, location_id, language_id, keywords, page_url, limit)
                if tmp.empty:
                    title_frame = 'null_result_{}.csv'.format(uuid.uuid4())
                    tmp.to_csv(title_frame, index = False)
                else:
                    plan_metrics(client, customer_id, location_id, tmp)


def create_ideas(client, customer_id, location_id, language_id, keyword, page_url, limit):
    info = ['date', 'location_id', 'language', 'network', 'keyword_seed', 'url_seed']
    info_content = [today, int(location_id), _DEFAULT_LANGUAGE, search_network.lower(), np.nan, np.nan]
    basic = pd.DataFrame(columns = info).reindex(columns = info)

    orders = ['keywords', 'avg_month_search', 'competition_level']
    res = pd.DataFrame(columns = orders).reindex(columns = orders)
    
    #if page_url:
    #    url_name = page_url if not page_url.startswith('https') else page_url[8:]
    #else:
    #    url_name = ''
    #title_basic = '{}_basic.csv'.format(keyword[0] if keyword else url_name)
    #title_res = '{}_historic.csv'.format(keyword[0] if keyword else url_name)

    keyword_plan_idea_service = client.get_service('KeywordPlanIdeaService',
                                                   version='v2')
    keyword_competition_level_enum = (
        client.get_type('KeywordPlanCompetitionLevelEnum', version='v2')
        .KeywordPlanCompetitionLevel)
    keyword_plan_network = client.get_type(
        'KeywordPlanNetworkEnum', version='v2').KeywordPlanNetwork.Value(search_network)
    logging.info('Location id here is {}'.format(location_id))
    location = map_locations_to_string_values(client, location_id)
    language = map_language_to_string_value(client, language_id)

    url_seed = None
    keyword_seed = None
    keyword_url_seed = None
    '''
    if not (keyword or page_url):
        raise ValueError('At least one of keywords or page URL is required, '
                         'but neither was specified.')
    '''
    if not keyword and page_url:
        logging.info('The url seed is {}'.format(page_url))
        info_content[-1] = page_url
        url_seed = client.get_type('UrlSeed', version='v2')
        url_seed.url.value = page_url

    if keyword and not page_url:
        logging.info('The keyword seed is {}'.format(keyword[0]))
        info_content[-2] = keyword[0]
        keyword_seed = client.get_type('KeywordSeed', version='v2')
        keyword_protos = map_keywords_to_string_values(client, keyword)
        keyword_seed.keywords.extend(keyword_protos)
    '''
    if keyword and page_url:
        keyword_url_seed = client.get_type('KeywordAndUrlSeed', version='v2')
        keyword_url_seed.url.value = page_url
        keyword_protos = map_keywords_to_string_values(client, keyword)
        keyword_url_seed.keywords.extend(keyword_protos)
    '''
    try:
        keyword_ideas = keyword_plan_idea_service.generate_keyword_ideas(
            customer_id, language, location, keyword_plan_network,
            url_seed = url_seed, keyword_seed = keyword_seed,
            keyword_and_url_seed = keyword_url_seed)
    
    except GoogleAdsException as ex:
        # record errors and return null dataframe
        logging.warning('Request with ID "{}" failed with status "{}" and includes the '
              'following errors:'.format(ex.request_id, ex.error.code().name))
              
        for error in ex.failure.errors:
            logging.warning('\tError with message "{}".'.format(error.message))
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    logging.warning('\t\tOn field: {}'.format(field_path_element.field_name))
        
        # null dataframe
        return basic
        
    l = limit if limit <= len(keyword_ideas.results) else len(keyword_ideas.results)

    for i, col in enumerate(info):
        basic[col] = [info_content[i]] * l
    
    for idea in keyword_ideas.results:
        competition_value = keyword_competition_level_enum.Name(
            idea.keyword_idea_metrics.competition).lower()

        each_row = pd.DataFrame([[idea.text.value, idea.keyword_idea_metrics.avg_monthly_searches.value, competition_value]],
                       columns = orders)
        
        res = res.append(each_row, ignore_index = True)
        if len(res) == l:
            break

    res = basic.join(res)
    #basic.to_csv(title_basic, index = False)
    #res.to_csv(title_res, index = False)
    
    return res


def plan_metrics(client, customer_id, location_id, frame):
    # step1
    # create plan with plan id
    keyword_plan = create_keyword_plan(client, customer_id)
    logging.info('Forecasting period is {}'.format(F_interval))
    keyword_plan_campaign = create_keyword_plan_campaign(client, customer_id, location_id,
                                                         keyword_plan[0])
    keyword_plan_ad_group = create_keyword_plan_ad_group(client, customer_id,
                                                         keyword_plan_campaign)
    
    if not isinstance(frame.url_seed[0], str):
        logging.info('forecasts of seed {}'.format(frame.keyword_seed[0]))
        title_res1 = 'keyword_result_{}.csv'.format(uuid.uuid4())
    
    else:
        logging.info('forecasts of seed {}'.format(frame.url_seed[0]))
        title_res1 = 'url_result_{}.csv'.format(uuid.uuid4())

    Ideas = frame.keywords # whole list of ideas
    indices = []
    for i in range(len(Ideas)):
        ind = create_keyword_plan_keywords(client, customer_id, keyword_plan_ad_group, Ideas[i])
        indices.append(ind)

    frame = frame.join(pd.Series(np.array(indices), name = 'ind'))

    # step2
    # generate forecast for each keyword(idea)
    keyword_plan_service = client.get_service('KeywordPlanService')
    resource_name = keyword_plan_service.keyword_plan_path(customer_id,
                                                           keyword_plan[1])

    try:
        response = keyword_plan_service.generate_forecast_metrics(resource_name)
    except GoogleAdsException as ex:
        # record errors
        logging.warning('Request with ID "{}" failed with status "{}" and includes the '
              'following errors:'.format(ex.request_id, ex.error.code().name))
              
        for error in ex.failure.errors:
            logging.warning('\tError with message "{}".'.format(error.message))
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    logging.warning('\t\tOn field: {}'.format(field_path_element.field_name))
    
    if len(response.keyword_forecasts) % 3 != 0:
        logging.warning('Some keywords do not support certain match types')
        title_frame = 'null_result_{}.csv'.format(uuid.uuid4())
        frame.to_csv(title_frame, index = False)
    
    else:
        tmp = np.zeros((1, 5))
        stats, stats_indices = [], []
    
        for i, forecast in enumerate(response.keyword_forecasts):
            # print('#{} Keyword ID: {}'.format(i + 1,
            #  forecast.keyword_plan_ad_group_keyword.value))

            if i % 3 == 0:
                stats_indices.append(forecast.keyword_plan_ad_group_keyword.value.split('/')[-1])

            metrics = forecast.keyword_forecast

            click_val = round(metrics.clicks.value, 2) if metrics.clicks.value else 0

            imp_val = round(metrics.impressions.value, 2) if metrics.impressions.value else 0
        
            cost_val = round(metrics.cost_micros.value / 1000000, 2) if metrics.cost_micros.value else 0
        
            ctr_val, cpc_val = 0, 0 

            vals = np.array([[click_val, imp_val, cost_val, ctr_val, cpc_val]])
            tmp += vals
            if (i + 1) % 3 == 0:
                tmp[0][-1] = round(tmp[0][2] / tmp[0][0], 2) if tmp[0][0] != 0 else 0
                tmp[0][-2] = round(tmp[0][0] / tmp[0][1], 2) if tmp[0][1] != 0 else 0
                stats += [tmp]
                tmp = np.zeros((1, 5))
    
        # assert len(stats) == len(Ideas)
        add_ord = ['clicks', 'impressions', 'cost', 'ctr', 'avg_cpc']
        stats = pd.DataFrame(np.asarray(stats).reshape(len(Ideas), -1), columns = add_ord).reindex(columns = add_ord)
        # stats.ctr = stats.ctr.astype(str) + '%'
        stats = stats.join(pd.Series(np.array(stats_indices), name = 'ind'))
    
        res1 = frame.merge(stats, left_on='ind', right_on='ind')
        res1.drop(['ind'], axis = 1, inplace = True)
        res1.to_csv(title_res1, index = False)


def map_keywords_to_string_values(client, keywords):
    keyword_protos = []
    for keyword in keywords:
        string_val = client.get_type('StringValue')
        string_val.value = keyword
        keyword_protos.append(string_val)
    return keyword_protos


def map_locations_to_string_values(client, location_id):
    gtc_service = client.get_service('GeoTargetConstantService', version='v2')
    
    location = client.get_type('StringValue')
    location.value = gtc_service.geo_target_constant_path(location_id)

    return [location]


def map_language_to_string_value(client, language_id):
    language = client.get_type('StringValue')
    language.value = client.get_service('LanguageConstantService',
                                        version='v2').language_constant_path(
                                            language_id)
    return language


def create_keyword_plan(client, customer_id):
    operation = client.get_type('KeywordPlanOperation', version='v2')
    keyword_plan = operation.create

    keyword_plan.name.value = ('Keyword plan for traffic estimate {}'.format(
        uuid.uuid4()))

    forecast_interval = client.get_type('KeywordPlanForecastIntervalEnum',
                                        version='v2').KeywordPlanForecastInterval.Value(F_interval)
    keyword_plan.forecast_period.date_interval = forecast_interval

    keyword_plan_service = client.get_service('KeywordPlanService',
                                              version='v2')
    response = keyword_plan_service.mutate_keyword_plans(customer_id,
                                                         [operation])
    resource_name = response.results[0].resource_name

    return resource_name, int(resource_name.split('/')[-1])


def create_keyword_plan_campaign(client, customer_id, location_id, keyword_plan):
    operation = client.get_type('KeywordPlanCampaignOperation', version='v2')
    keyword_plan_campaign = operation.create

    keyword_plan_campaign.name.value = 'Keyword plan campaign {}'.format(
        uuid.uuid4())
    keyword_plan_campaign.cpc_bid_micros.value = 1000000
    keyword_plan_campaign.keyword_plan.value = keyword_plan

    keyword_plan_network = client.get_type('KeywordPlanNetworkEnum',
                                           version='v2')
    network = keyword_plan_network.KeywordPlanNetwork.Value(search_network) 
    keyword_plan_campaign.keyword_plan_network = network

    geo_target = client.get_type('KeywordPlanGeoTarget', version='v2')
    # Specified location
    geo_target.geo_target_constant.value = 'geoTargetConstants/' + location_id
    keyword_plan_campaign.geo_targets.extend([geo_target])

    language = client.get_type('StringValue', version='v2')
    # Constant for English
    language.value = 'languageConstants/1000'
    keyword_plan_campaign.language_constants.extend([language])

    keyword_plan_campaign_service = client.get_service(
        'KeywordPlanCampaignService', version='v2')
    response = keyword_plan_campaign_service.mutate_keyword_plan_campaigns(
        customer_id, [operation])

    resource_name = response.results[0].resource_name

    return resource_name


def create_keyword_plan_ad_group(client, customer_id, keyword_plan_campaign):
    operation = client.get_type('KeywordPlanAdGroupOperation', version='v2')
    keyword_plan_ad_group = operation.create

    keyword_plan_ad_group.name.value = 'Keyword plan ad group {}'.format(
        uuid.uuid4())
    keyword_plan_ad_group.cpc_bid_micros.value = 2500000
    keyword_plan_ad_group.keyword_plan_campaign.value = keyword_plan_campaign

    keyword_plan_ad_group_service = client.get_service(
        'KeywordPlanAdGroupService', version='v2')
    response = keyword_plan_ad_group_service.mutate_keyword_plan_ad_groups(
        customer_id, [operation])

    resource_name = response.results[0].resource_name

    return resource_name


def create_keyword_plan_keywords(client, customer_id, plan_ad_group, idea):
    match_types = client.get_type('KeywordMatchTypeEnum', version='v2')
    # The system max cpc bid upper bound for a keyword is 100 USD
    upper_bound = 100000000

    keyword_plan_keyword1 = client.get_type('KeywordPlanKeyword', version='v2')
    keyword_plan_keyword1.text.value = idea
    keyword_plan_keyword1.cpc_bid_micros.value = upper_bound
    keyword_plan_keyword1.match_type = match_types.BROAD
    keyword_plan_keyword1.keyword_plan_ad_group.value = plan_ad_group

    keyword_plan_keyword2 = client.get_type('KeywordPlanKeyword', version='v2')
    keyword_plan_keyword2.text.value = idea
    keyword_plan_keyword2.cpc_bid_micros.value = upper_bound
    keyword_plan_keyword2.match_type = match_types.PHRASE
    keyword_plan_keyword2.keyword_plan_ad_group.value = plan_ad_group

    keyword_plan_keyword3 = client.get_type('KeywordPlanKeyword', version='v2')
    keyword_plan_keyword3.text.value = idea
    keyword_plan_keyword3.cpc_bid_micros.value = upper_bound
    keyword_plan_keyword3.match_type = match_types.EXACT
    keyword_plan_keyword3.keyword_plan_ad_group.value = plan_ad_group


    operations = []
    for keyword in [keyword_plan_keyword1,
                    keyword_plan_keyword2,
                    keyword_plan_keyword3]:
        operation = client.get_type('KeywordPlanKeywordOperation', version='v2')
        operation.create.CopyFrom(keyword)
        operations.append(operation)

    keyword_plan_keyword_service = client.get_service(
        'KeywordPlanKeywordService', version='v2')
    response = keyword_plan_keyword_service.mutate_keyword_plan_keywords(
        customer_id, operations)
    
    ind = response.results[0].resource_name.split('/')[-1]
    #for result in response.results:
    #    print('Created keyword plan keyword with resource name: {}'.format(
    #        result.resource_name))
    return ind

if __name__ == '__main__':
    google_ads_client = GoogleAdsClient.load_from_storage('/Users/xlyue/Documents/google-ads-python-master/google-ads.yaml')
    '''
    parser = argparse.ArgumentParser(
        description='Combo.')
    # The following argument(s) should be provided to run the example.
    
    parser.add_argument('-c', '--customer_id', type=six.text_type,
                        required=True, help='The Google Ads customer ID.')
    
    parser.add_argument('-k', '--keywords', type=six.text_type, required=False,
                        help='Comma-delimited starter keywords')
    
    parser.add_argument('-l', '--location_ids', type=six.text_type,
                        required=False, help='Comma-delimited list of location '
                                             'criteria IDs')
    
    parser.add_argument('-i', '--language_id', type=six.text_type,
                        required=False, help='Comma-delimited list of language '
                                             'criterion IDs')
    
    parser.add_argument('-p', '--page_urls', type=six.text_type, required=False,
                        help='A URL string related to your business')
    

    parser.set_defaults(location_ids = _DEFAULT_LOCATION_IDS,
                        language_id = _DEFAULT_LANGUAGE_ID, keywords = '', page_urls = '')

    args = parser.parse_args()
    '''
    params = {'location_ids': _DEFAULT_LOCATION_IDS, 'language_id': _DEFAULT_LANGUAGE_ID, 'keywords': '', 'page_urls': '', 'limit': _DEFAULT_LIMIT}
    fileobj = open('../config/config.txt')
    
    for line in fileobj:
        line = line.strip()
        key_value = line.split('=')
        if key_value[1]:
            params[key_value[0]] = key_value[1]

    location_ids = [loc for loc in params['location_ids'].split(',') if loc]
    keywords = [keyword for keyword in params['keywords'].split(',') if keyword]
    page_urls = [url for url in params['page_urls'].split(',') if url]

    main(google_ads_client, params['customer_id'], location_ids, params['language_id'],
         keywords, page_urls, params['limit'])