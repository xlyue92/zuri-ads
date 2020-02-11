# KeywordPlan Script
## Initial Background Setup 

A [KeywordPlan](https://developers.google.com/google-ads/api/reference/rpc/google.ads.googleads.v2.resources#adgroup) which combines historical and forecasting metrics will be created based on GoogleAds API.

The plan is built in the way of:
```
KeywordPlan <-- KeywordPlan Campaign <-- KeywordPlan Adgroup <-- KeywordPlan Keywords
```
And **per plan** the number of each category are shown below:

| Name | Limitation | Setup |
|:----:|:----------:|:-----:|
| Plan | 1 | ForecastPeriod |
| Campaign | 1 | Plan, GeoTargets, Language, Network |
| Adgroup | 200 | Campaign |
| Keywords | 2500 | Adgroup, MatchType |

In order to make stable prediction for each of the keywords ideas without other influence (e.g. combination of different keywords in each adgroup will affect each other in the metrics prediction performance), we will write the initial script for a KeywordPlan with only one keyword in each adgroup. In other words, 200 keywords will be included in total under the campaign created for the plan.

### Remark:

* A complete keyword forecasting consists of 3 MatchTypes: Broad, Exact and Phrase. 

  Type **Unspecified** is not allowed in the forecasting.
  
* Max bid cpc of keywords, adgroups and campaign are not necessarily related. 

  Max bid cpc of keywords overrides that of adgroups.
  
  [Bid cpc](https://groups.google.com/forum/#!topic/adwords-api/Fr0zTvzuEAg) is shown in the way of **cpc_bid_micros**, 1,000,000 microns = 1 USD or the account currency.
  
  Different from Adwords API, the minimum Max bid cpc is 10000 microns = 0.01 USD or the account currency.
