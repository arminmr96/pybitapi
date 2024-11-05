import requests
import json
from pybitapi import utils
from pybitapi.variables import *

class Client():
   
    def __init__(self, api_key, api_secret, passphrase):
       
        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.PASSPHRASE = passphrase
      
    def _request(self, method, request_path, data):
        if method == GET:
            request_path = request_path + utils.parse_params_to_str(data)
            
        # Create url
        url = API_URL + request_path
        
        # Get local time
        timestamp = utils.get_timestamp()
        
        body = json.dumps(data) if method == POST else ""
        sign = utils.sign(utils.pre_hash(timestamp, method, request_path, str(body)), self.API_SECRET)
        header = utils.get_header(self.API_KEY, sign, timestamp, self.PASSPHRASE)
        
        # Send request
        response = None
        if method == GET:
            response = requests.get(url, headers=header)
        elif method == POST:
            response = requests.post(url, data=body, headers=header)
            
        # Exception handle
        if not str(response.status_code).startswith('2'):
            raise Exception(f"API Request Error: status code ({response.status_code}): {response.json()}")

        return response.json()
    
    def _create_request(self, required_params, optional_params, type, category, endpoint, method, params):
        
        # Initialize data
        data = {}
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in params:
                raise ValueError(f"The '{param}' parameter is required.") 
            else:
                data[param] = params[param]
        
        # Check if eather orderId and clientOid are provided
        if "orderId" in optional_params and "clientOid" in optional_params:
            orderId = params.get("orderId")
            clientOid = params.get("clientOid") 
            
            if orderId or clientOid:
                pass
            else:
                raise ValueError("Either 'orderId' or 'clientOid' is required.")          
        
        # Add optional parameters if provided
        for key, value in params.items():
            if key in optional_params:
                data[key] = value
        
        request_path = API_VERSION + type + "/" + category + "/" + endpoint  
            
        return self._request(method, request_path, data)
            
    # ########################################
    # ############## SPOT MARKET #############
    # ########################################
    
    def spot_coin_info(self, **params):
        
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = ["coin"]
        
        # Request parameters
        type = SPOT
        category = PUBLIC
        endpoint = "coins"
        method = GET
 
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
        
    def spot_symbol_info(self, **params):
        
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = ["symbol"]
        
        # Request parameters
        type = SPOT
        category = PUBLIC
        endpoint = "symbols"
        method = GET

        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
        
    def spot_vip_fee_rate(self, **params):
        
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = SPOT
        category = MARKET
        endpoint = "vip-fee-rate"
        method = GET

        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
        
    def spot_ticker_info(self, **params):
        
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = ["symbol"]
        
        # Request parameters
        type = SPOT
        category = MARKET
        endpoint = "tickers"
        method = GET

        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)        
        
    def spot_merge_depth(self, **params):
        
        # List of required parameters
        required_params = ["symbol"]
        
        # List of optional parameters
        optional_params = ["precision", "limit"]
        
        # Request parameters
        type = SPOT
        category = MARKET
        endpoint = "merge-depth"
        method = GET

        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)        
        
    def spot_orderbook_depth(self, **params):
        
        # List of required parameters
        required_params = ["symbol"]
        
        # List of optional parameters
        optional_params = ["type", "limit"]
        
        # Request parameters
        type = SPOT
        category = MARKET
        endpoint = "orderbook"
        method = GET

        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)        

    def spot_candlestick_data(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "granularity"]
        
        # List of optional parameters
        optional_params = ["startTime", "endTime", "limit"]
        
        # Request parameters
        type = SPOT
        category = MARKET
        endpoint = "candles"
        method = GET

        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)            
    
    def spot_history_candlestick_data(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "granularity", "endTime"]
        
        # List of optional parameters
        optional_params = ["limit"]
        
        # Request parameters
        type = SPOT
        category = MARKET
        endpoint = "history-candles"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def spot_recent_trades(self, **params):
        
        # List of required parameters
        required_params = ["symbol"]
        
        # List of optional parameters
        optional_params = ["limit"]
        
        # Request parameters
        type = SPOT
        category = MARKET
        endpoint = "fills"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)        
    
    def spot_market_trades(self, **params):
        
        # List of required parameters
        required_params = ["symbol"]
        
        # List of optional parameters
        optional_params = ["limit", "idLessThan", "startTime", "endTime"]
        
        # Request parameters
        type = SPOT
        category = MARKET
        endpoint = "fills-history"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)        

    # ########################################
    # ############## SPOT TRADE ##############
    # ########################################
    
    def spot_place_order(self, **params):
  
        # List of required parameters
        required_params = ["symbol", "side", "orderType", "force", "size"]
        
        # List of optional parameters
        optional_params = [
            "price", "clientOid", "triggerPrice", "tpslType", "requestTime",
            "receiveWindow", "stpMode", "presetTakeProfitPrice",
            "executeTakeProfitPrice", "presetStopLossPrice", "executeStopLossPrice"
        ]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "plase-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)        
    
    def spot_cancel_replace_order(self, **params):
  
        # List of required parameters
        required_params = ["symbol", "price", "size"]
        
        # List of optional parameters
        optional_params = [
            "clientOid", "orderId", "newClientOid", "presetTakeProfitPrice",
            "executeTakeProfitPrice", "presetStopLossPrice", "executeStopLossPrice"
        ]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "cancel-replace-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                        
    
    def spot_cancel_order(self, **params):
  
        # List of required parameters
        required_params = ["symbol"]
        
        # List of optional parameters
        optional_params = ["tpslType", "orderId", "clientOid"]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "cancel-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)        

    def spot_batch_place_order(self, **params):
  
        # List of required parameters
        required_params = ["orderList", "side", "orderType", "force", "size"]
        
        # List of optional parameters
        optional_params = [
            "symbol", "batchMode", "price", "clientOid", "stpMode", "presetTakeProfitPrice",
            "executeTakeProfitPrice", "presetStopLossPrice", "executeStopLossPrice"
        ]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "batch-orders"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                        

    def spot_batch_cancel_replace_order(self, **params):
  
        # List of required parameters
        required_params = ["orderList", "symbol", "price", "size"]
        
        # List of optional parameters
        optional_params = [
            "clientOid", "orderId", "newClientOid", "presetTakeProfitPrice",
            "executeTakeProfitPrice", "presetStopLossPrice", "executeStopLossPrice"
        ]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "batch-cancel-replace-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                        

    def spot_batch_cancel_order(self, **params):
  
        # List of required parameters
        required_params = ["orderList"]
        
        # List of optional parameters
        optional_params = ["symbol", "batchMode", "orderId", "clientOid"]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "batch-cancel-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_cancel_order_symbol(self, **params):
  
        # List of required parameters
        required_params = ["symbol"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "cancel-symbol-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                
    
    def spot_order_info(self, **params):
  
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = ["orderId", "clientOid", "requestTime", "receiveWindow"]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "orderInfo"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_current_orders(self, **params):
  
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = [
            "symbol", "startTime", "endTime", "idLessThan", "limit",
            "orderId", "tpslType", "requestTime", "receiveWindow",        
        ]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "unfilled-orders"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_history_orders(self, **params):
  
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = [
            "symbol", "startTime", "endTime", "idLessThan", "limit",
            "orderId", "tpslType", "requestTime", "receiveWindow",            
        ]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "history-orders"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_fills(self, **params):
  
        # List of required parameters
        required_params = ["symbol"]
        
        # List of optional parameters
        optional_params = ["orderId", "startTime", "endTime", "limit", "idLessThan"]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "fills"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    # ########################################
    # ############# SPOT TRIGGER #############
    # ########################################
    
    def spot_place_plan_order(self, **params):
  
        # List of required parameters
        required_params = [
            "symbol", "side", "triggerPrice", "orderType", "size", "triggerType"
        ]
        
        # List of optional parameters
        optional_params = [
            "executePrice", "planType", "clientOid", "force", "stpMode"          
        ]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "place-plan-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_modify_plan_order(self, **params):
  
        # List of required parameters
        required_params = ["triggerPrice", "orderType", "size"]
        
        # List of optional parameters
        optional_params = ["orderId", "clientOid", "executePrice"]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "modify-plan-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                
    
    def spot_cancel_plan_order(self, **params):
  
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = ["orderId", "clientOid"]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "cancel-plan-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_get_current_plan_orders(self, **params):
  
        # List of required parameters
        required_params = ["symbol"]
        
        # List of optional parameters
        optional_params = ["limit", "idLessThan", "startTime", "endTime"]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "current-plan-order"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_get_plan_sub_order(self, **params):
  
        # List of required parameters
        required_params = ["planOrderId"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "plan-sub-order"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_get_history_plan_orders(self, **params):
  
        # List of required parameters
        required_params = ["symbol", "startTime", "endTime"]
        
        # List of optional parameters
        optional_params = ["limit"]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "history-plan-order"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_batch_cancel_plan_order(self, **params):
  
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = ["symbolList"]
        
        # Request parameters
        type = SPOT
        category = TRADE
        endpoint = "batch-cancel-plan-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    # ########################################
    # ############# SPOT ACCOUNT #############
    # ########################################    
    
    def spot_get_account_info(self, **params):
  
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = SPOT
        category = ACCOUNT
        endpoint = "info"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                
    
    def spot_get_account_assets(self, **params):
  
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = ["coin", "assetType"]
        
        # Request parameters
        type = SPOT
        category = ACCOUNT
        endpoint = "assets"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_get_sub_account_assets(self, **params):
  
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = SPOT
        category = ACCOUNT
        endpoint = "subaccount-assets"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_modify_deposit_account(self, **params):
  
        # List of required parameters
        required_params = ["accountType", "coin"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = SPOT
        category = ACCOUNT
        endpoint = "modify-deposit-account"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_get_account_bills(self, **params):
  
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = [
            "coin", "groupType", "businessType", "startTime",
            "endTime", "limit", "idLessThan"
        ]
        
        # Request parameters
        type = SPOT
        category = ACCOUNT
        endpoint = "bills"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                
        
    def spot_transfer(self, **params):
  
        # List of required parameters
        required_params = ["fromType", "toType", "amount", "coin", "symbol"]
        
        # List of optional parameters
        optional_params = ["clientOid"]
        
        # Request parameters
        type = SPOT
        category = WALLET
        endpoint = "transfer"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_get_transferable_coin_list(self, **params):
  
        # List of required parameters
        required_params = ["fromType", "toType"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = SPOT
        category = WALLET
        endpoint = "transfer-coin-info"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_sub_transfer(self, **params):
  
        # List of required parameters
        required_params = [
            "fromType", "toType", "amount",
            "coin", "fromUserId", "toUserId"
        ]
        
        # List of optional parameters
        optional_params = ["symbol", "clientOid"]
        
        # Request parameters
        type = SPOT
        category = WALLET
        endpoint = "subaccount-transfer"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                
    
    def spot_withdraw(self, **params):
  
        # List of required parameters
        required_params = ["coin", "transferType", "address", "size"]
        
        # List of optional parameters
        optional_params = [
            "chain", "innerToType", "areaCode", "tag", "remark", "clientOid"
        ]
        
        # Request parameters
        type = SPOT
        category = WALLET
        endpoint = "withdrawal"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_get_mainsub_transfer_record(self, **params):
    
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = [
            "coin", "role", "subUid", "startTime",
            "endTime", "clientOid", "limit", "idLessThan"
        ]
        
        # Request parameters
        type = SPOT
        category = ACCOUNT
        endpoint = "sub-main-trans-record"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                

    def spot_get_transfer_record(self, **params):
    
        # List of required parameters
        required_params = ["coin", "fromType"]
        
        # List of optional parameters
        optional_params = ["startTime", "endTime", "clientOid", "limit", "idLessThan"]
        
        # Request parameters
        type = SPOT
        category = ACCOUNT
        endpoint = "transferRecords"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)                
        
    def spot_switch_BGB_deduct(self, **params):
        
        # List of required parameters
        required_params = ["deduct"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = SPOT
        category = ACCOUNT
        endpoint = "switch-deduct"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
        
    def spot_get_deposit_address(self, **params):
        
        # List of required parameters
        required_params = ["coin"]
        
        # List of optional parameters
        optional_params = ["chain", "size"]
        
        # Request parameters
        type = SPOT
        category = WALLET
        endpoint = "deposit-address"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def spot_get_subaccount_deposit_address(self, **params):
        
        # List of required parameters
        required_params = ["subUid", "coin"]
        
        # List of optional parameters
        optional_params = ["chain", "size"]
        
        # Request parameters
        type = SPOT
        category = WALLET
        endpoint = "subaccount-deposit-address"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def spot_get_BGB_deduct_info(self, **params):
        
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = SPOT
        category = ACCOUNT
        endpoint = "deduct-info"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def  spot_cancel_withdrawal(self, **params):
        
        # List of required parameters
        required_params = ["orderId"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = SPOT
        category = WALLET
        endpoint = "cancel-withdrawal"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def spot_get_subaccount_deposit_records(self, **params):
        
        # List of required parameters
        required_params = ["subUid"]
        
        # List of optional parameters
        optional_params = ["coin", "startTime", "endTime", "idLessThan", "limit"]
        
        # Request parameters
        type = SPOT
        category = WALLET
        endpoint = "subaccount-deposit-records"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def spot_get_withdrawal_records(self, **params):
        
        # List of required parameters
        required_params = ["startTime", "endTime"]
        
        # List of optional parameters
        optional_params = ["coin", "clientOid", "idLessThan", "orderId", "limit"]
        
        # Request parameters
        type = SPOT
        category = WALLET
        endpoint = "withdrawal-records"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def spot_get_deposit_records(self, **params):
        
        # List of required parameters
        required_params = ["startTime", "endTime"]
        
        # List of optional parameters
        optional_params = ["coin", "orderId", "idLessThan", "limit"]
        
        # Request parameters
        type = SPOT
        category = WALLET
        endpoint = "deposit-records"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    # ########################################
    # ############ FUTURE MARKET #############
    # ########################################
    
    def mix_vip_fee_rate(self, **params):
        
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "vip-fee-rate"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_interest_rate_history(self, **params):
        
        # List of required parameters
        required_params = ["coin"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "union-interest-rate-history"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_interest_exchange_rate(self, **params):
        
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "exchange-rate"
        method = GET  
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_discount_rate(self, **params):
        
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "discount-rate"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_merge_market_depth(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType"]
        
        # List of optional parameters
        optional_params = ["precision", "limit"]
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "merge-depth"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_ticker(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "ticker"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_all_tickers(self, **params):
        
        # List of required parameters
        required_params = ["productType"]

        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "tickers"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
             
    def mix_recent_transactions(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType"]
        
        # List of optional parameters
        optional_params = ["limit"]
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "fills"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_history_transactions(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType"]
        
        # List of optional parameters
        optional_params = ["limit", "idLessThan", "startTime", "endTime"]
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "fills-history"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_candlestick_data(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType", "granularity"]
        
        # List of optional parameters
        optional_params = ["startTime", "endTime", "kLineType", "limit"]
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "candles"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_historical_candlestick(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType", "granularity"]
        
        # List of optional parameters
        optional_params = ["startTime", "endTime", "limit"]
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "history-candles"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
            
    def mix_historical_index_price_candlestick(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType", "granularity"]
        
        # List of optional parameters
        optional_params = ["startTime", "endTime", "limit"]
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "history-index-candles"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_historical_mark_price_candlestick(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType", "granularity"]
        
        # List of optional parameters
        optional_params = ["startTime", "endTime", "limit"]
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "history-mark-candles"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
        
    def mix_open_interest(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "open-interest"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)    
        
    def mix_next_funding_time(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "funding-time"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_mark_index_market_prices(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "symbol-price"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_historical_funding_rates(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType"]
        
        # List of optional parameters
        optional_params = ["pageSize", "pageNo"]
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "history-fund-rate"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_current_funding_rate(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "current-funding-rate"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_contract_config(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = ["symbol"]
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "contracts"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    # ########################################
    # ############ FUTURE TRADE ##############
    # ########################################
    
    def mix_place_order(self, **params):
        
        # List of required parameters
        required_params = [
            "symbol", "productType", "marginMode", "marginCoin",
            "size", "side", "orderType"
        ]
        
        # List of optional parameters
        optional_params = [
            "price", "tradeSide", "force", "clientOid", "reduceOnly", 
            "presetStopSurplusPrice", "presetStopLossPrice", "priceProtect"
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "place_order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_reversal(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "marginCoin", "productType", "size"]
        
        # List of optional parameters
        optional_params = ["side", "tradeSide", "clientOid"]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "click-backhand"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_batch_order(self, **params):
        
        # List of required parameters
        required_params = [
            "symbol", "productType", "marginMode", "marginCoin", 
            "orderList", "size", "side", "orderType", 
        ]
        
        # List of optional parameters
        optional_params = [
            "price", "tradeSide", "force", "clientOid", "reduceOnly"
            "presetStopSurplusPrice", "presetStopLossPrice", "stpMode"
            
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "batch-place-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_modify_order(self, **params):
      
        # List of required parameters
        required_params = ["symbol", "productType", "newClientOid" ]
        
        # List of optional parameters
        optional_params = [
            "orderId", "clientOid", "newSize", "newPrice",
            "newPresetStopSurplusPrice", "newPresetStopLossPrice"            
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "modify-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_cancel_order(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType"]
        
        # List of optional parameters
        optional_params = ["marginCoin", "orderId", "clientOid"]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "cancel-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_batch_cancel(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = ["orderIdList", "orderId", "clientOid", "symbol", "marginCoin"]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "batch-cancel-orders"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_flash_close_position(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = ["symbol", "holdSide"]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "close-positions"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_get_order_detail(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType"]
        
        # List of optional parameters
        optional_params = ["orderId", "clientOid"]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "detail"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_get_order_fill_details(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = [
            "orderId", "symbol", "idLessThan", 
            "startTime", "endTime", "limit"
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "fill-detail"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_get_historical_transaction_details(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = [
            "orderId", "symbol", "startTime",
            "endTime", "idLessThan", "limit"
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "fill-history"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_get_pending_orders(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = [
            "orderId", "clientOid", "symbol", "status",
            "idLessThan", "startTime", "endTime", "limit"
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "orders-pending"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_get_history_order(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = [
            "orderId", "clientOid", "symbol", "idLessThan",
            "orderSource", "startTime", "endTime", "limit"
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "orders-history"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_cancel_all_orders(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = ["symbol", "marginCoin", "requestTime", "receiveWindow"]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "cancel-all-orders"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    # ########################################
    # ########### FUTURE TRIGGER #############
    # ######################################## 
    
    def mix_trigger_sub_order(self, **params):
        
        # List of required parameters
        required_params = ["planType", "planOrderId", "productType"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "plan-sub-order"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_stop_profit_and_stop_loss_plan_orders(self, **params):
        
        # List of required parameters
        required_params = [
            "marginCoin", "productType", "symbol", 
            "clientOid", "stpMode",
        ]
        
        # List of optional parameters
        optional_params = [
            "triggerType", "executePrice", "rangeRate", 
            "triggerBy", "triggerTime", "orderSource", "orderTime"
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "place-tpsl-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_place_trigger_order(self, **params):
        
        # List of required parameters
        required_params = [
            "planType", "symbol", "productType", "marginMode", "marginCoin", 
            "size", "triggerPrice", "triggerType", "side", "orderType"
        ]
        
        # List of optional parameters
        optional_params = [
            "price", "callbackRatio", "tradeSide", "clientOid",
            "reduceOnly", "stopSurplusTriggerPrice", "stopSurplusExecutePrice",
            "stopSurplusTriggerType", "stopLossTriggerPrice", "stopLossExecutePrice",
            "stopLossTriggerType", "stpMode"
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "place-plan-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_modify_stop_profit_and_stop_loss_plan_order(self, **params):
        
        # List of required parameters
        required_params = ["marginCoin", "productType", "symbol", "triggerPrice", "size"]
        
        # List of optional parameters
        optional_params = ["orderId", "clientOid", "triggerType", "executePrice", "rangeRate"]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "modify-tpsl-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
      
    def mix_modify_trigger_order(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = [
            "orderId", "clientOid", "newSize", "newPrice", 
            "newCallbackRatio", "newTriggerPrice", "newTriggerType",
            "newStopSurplusTriggerPrice", "newStopSurplusExecutePrice",
            "newStopSurplusTriggerType", "newStopLossTriggerPrice",
            "newStopLossExecutePrice", "newStopLossTriggerType",
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "modify-plan-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_get_pending_trigger_order(self, **params):
        
        # List of required parameters
        required_params = ["planType", "productType"]
        
        # List of optional parameters
        optional_params = [
            "orderId", "clientOid", "symbol", "idLessThan",
            "startTime", "endTime", "limit"
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "orders-plan-pending"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_cancel_trigger_order(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = [
            "orderIdList", "orderId", "clientOid", "symbol", "marginCoin", "planType"
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "cancel-plan-order"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_get_history_trigger_order(self, **params):
        
        # List of required parameters
        required_params = ["planType", "productType"]
        
        # List of optional parameters
        optional_params = [
            "orderId", "clientOid", "planStatus", "symbol",
            "idLessThan", "startTime", "endTime", "limit"
        ]
        
        # Request parameters
        type = MIX
        category = ORDER
        endpoint = "orders-plan-history"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    # ########################################
    # ########### FUTURE ACCOUNT #############
    # ########################################     
    
    def mix_get_single_account(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType", "marginCoin"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "account"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_get_account_list(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "accounts"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_get_subaccount_assets(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "sub-account-assets"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_get_USDTM_futures_interest_history(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = ["coin", "idLessThan", "startTime", "endTime", "limit"]
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "interest-history"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_my_estimated_open_count(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType", "marginCoin","openAmount", "openPrice"]
        
        # List of optional parameters
        optional_params = ["leverage"]
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "open-count"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_set_isolated_position_auto_margin(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "autoMargin", "marginCoin"]
        
        # List of optional parameters
        optional_params = ["holdSide", "amount"]
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "set-auto-margin"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_change_leverage(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType", "marginCoin", "leverage"]
        
        # List of optional parameters
        optional_params = ["holdSide"]
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "set-leverage"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_adjust_position_margin(self, **params):    
        
        # List of required parameters
        required_params = ["symbol", "productType", "marginCoin", "holdSide", "amount"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "set-margin"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_set_USDTM_futures_asset_mode(self, **params):
        
        # List of required parameters
        required_params = ["productType", "assetMode"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "set-asset-mode"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_change_margin_mode(self, **params):
        
        # List of required parameters
        required_params = ["symbol", "productType", "marginCoin", "marginMode"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "set-margin-mode"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_change_position_mode(self, **params):
        
        # List of required parameters
        required_params = ["productType", "posMode"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "set-position-mode"
        method = POST        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_get_account_bills(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = [
            "coin", "businessType", "idLessThan", 
            "startTime", "endTime", "limit"
        ]
        
        # Request parameters
        type = MIX
        category = ACCOUNT
        endpoint = "bill"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    # ########################################
    # ########### FUTURE POSITION ############
    # ########################################         
    
    def mix_position_tier(self, **params):
        
        # List of required parameters
        required_params = ["productType", "symbol"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = MARKET
        endpoint = "query-position-lever"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_single_position(self, **params):
        
        # List of required parameters
        required_params = ["productType", "symbol", "marginCoin"]
        
        # List of optional parameters
        optional_params = []
        
        # Request parameters
        type = MIX
        category = POSITION
        endpoint = "single-position"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_all_positions(self, **params):
        
        # List of required parameters
        required_params = ["productType"]
        
        # List of optional parameters
        optional_params = ["marginCoin"]
        
        # Request parameters
        type = MIX
        category = POSITION
        endpoint = "all-position"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    def mix_historical_position(self, **params):
        
        # List of required parameters
        required_params = []
        
        # List of optional parameters
        optional_params = [
            "symbol", "productType", "idLessThan",
            "startTime", "endTime", "limit"
        ]
        
        # Request parameters
        type = MIX
        category = POSITION
        endpoint = "history-position"
        method = GET        
        
        return self._create_request(required_params, optional_params, type, category, endpoint, method, params)
    
    