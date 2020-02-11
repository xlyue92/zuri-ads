# Zuri GoogleAds(Beta) Research
## [Metrics Definition](https://support.google.com/google-ads/topic/3121777?hl=en&ref_topic=3119071)
*  The way we build metrics is based on the common definition that Google gives us.


## Configuration Setup
1. Download [zuri ads repo](https://github.com/xlyue92/zuri-ads).

   (YAML file and other documents needed)

   Installation: 
   
   ```
   pip install google-ads
   ```
   
   
 2. Prerequisites for Configuration of YAML file:
   
 *  Developer Token
    
    Create/ sign in your [Manager account](https://ads.google.com/home/tools/manager-accounts/).
    
    Navigate to **TOOLS & SETTINGS > SETUP > API Center**, you will see your **Developer Token** in the **API Access** section.
    
 *  **Starting from the following step**
 
    Register a new test manager account [here](https://ads.google.com/um/Welcome/Home?a=1&sf=mt&authuser=0#ta) using a **different** email address(different Google account). You will see the red 'Test account' sign on the top right part of the user page.
    
    
 *  Client_id & Client_secret
    
    Enable Google Ads API in the [API library](https://console.developers.google.com/apis/library).
                               
    Open [Credentials](https://console.developers.google.com/apis/credentials) page, create or select a project.
                               
    Select **Create credentials > OAuth client ID > Other (Installed Application)** to create the client ID and client secret, then download the json file and save it in your prefered directory.
    
 *  Access Token & Refresh Token
 
    Insert your client id & secret in your ```google-ads.yaml``` file.
    
    Make sure you clone the [zuri-ads repo](https://github.com/xlyue92/zuri-ads), otherwise we start from 
    ```
    $ git clone https://github.com/xlyue92/zuri-ads-python.git
    $ cd zuri-ads-python
    $ pip install .
    ```
    
    Then continue with 
    ```
    $ python setup.py test
    ```
    Navigate to ``` authenticate_in_standalone_application.py```
    ```
    $ cd examples/authentication
    ```
    Find the json file path and run the following
    ```
    $ ./authenticate_in_standalone_application.py --client_secrets_path=/path/to/secrets.json
    ```
    Access the prompted URL from the example: 
    - Navigate to the URL in a private browser session or an incognito window.
    - Log in with the same Google account you use to access Ads(test manager account).
    - Click **Allow** on the OAuth2 consent screen.
    
    Copy and paste the authorization code shown to you in the command line and press enter to get two tokens. Then save the refresh token in the YAML file.
    
    Insert your test manager account (10 digits) number in the section of ```login_customer_id``` in your YAML file.
    
3. Verify your configuration
   
   Now you should be able to make calls to the Google Ads API. 
   
   Remember to add path to the YAML file in the ```google_ads_client``` part:
   
   **GoogleAdsClient will read the google-ads.yaml configuration file in the home directory if none is specified.**

   For instance, ```python3 GetCampaigns.py```.

   The console should print a listing of the campaigns in the subaccounts under your test manager account.

4. Implement src scripts
    ```
    $ cd zuri-ads-python/src
    $ python3 ideas_forecast.py
    ```
   And check the results.

    
    
    
   
