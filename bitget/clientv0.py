from bitget import utils
from bitget.variables import *
from bitget import logger

class Client():
   
    def __init__(self, api_key, api_secret, passphrase):
       
        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.passphrase = passphrase
      
    def _request(self, method, request_path, params={}):
        pass
    
    
    # ########################################
    # ################ SPOT MARKET############
    # ########################################
    
    def spot_coin_info(self, coin=None):
        
        if coin:
            params = {}
            params["coin"] = coin
            return self._request(GET, SPOT_PUBLIC_V2_URL + "/coins", params)
        else:
            return self._request(GET, SPOT_PUBLIC_V2_URL + "/coins")
        
    def spot_symbol_info(self, symbol=None):
        
        if symbol:
            params = {}
            params["symbol"] = symbol
            return self._request(GET, SPOT_PUBLIC_V2_URL + "/symbols", params)
        else:
            return self._request(GET, SPOT_PUBLIC_V2_URL + "/symbols")
    
    def spot_vip_fee_rate(self):
        
        return self._request(GET, SPOT_MARKET_V2_URL + "/vip-fee-rate")
    
    def spot_ticker_info(self, symbol=None):
        
        if symbol:
            params = {}
            params["symbol"] = symbol
            return self._request(GET, SPOT_MARKET_V2_URL + "/tickers", params)
        else:
            return self._request(GET, SPOT_MARKET_V2_URL + "/tickers")
    
    def spot_merge_depth(self, symbol, **kwargs):
        
        params = {}
        params["symbol"] = symbol
        
        # Define a set of valid optional parameters
        valid_options = {"precision", "limit"}
        
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(GET, SPOT_MARKET_V2_URL + "/merge-depth", params)
    
    def spot_orderbook_depth(self, symbol, **kwargs):
        
        params = {}
        params["symbol"] = symbol
        
        # Define a set of valid optional parameters
        valid_options = {"type", "limit"}
        
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(GET, SPOT_MARKET_V2_URL + "/orderbook", params)
    
    def spot_candlestick_data(self, **kwargs):
        
        # List of required parameters
        required_params = ["symbol", "granularity"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params}
        
        # Define a set of valid optional parameters
        valid_options = {"startTime", "endTime", "limit"}
        
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(GET, SPOT_MARKET_V2_URL + "/candles", params)
    
    def spot_history_candlestick_data(self, limit=None, **kwargs):
        
        # List of required parameters
        required_params = ["symbol", "granularity", "endTime"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params}
        
        if limit:
            params["limit"] = limit
            
        return self._request(GET, SPOT_MARKET_V2_URL + "/candles", params)
    
    def spot_recent_trades(self, symbol, limit=None):
        
        params = {}
        params["symbol"] = symbol
        if limit:
            params["limit"] = limit
            
        return self._request(GET, SPOT_MARKET_V2_URL + "/fills", params)
    
    def spot_market_trades(self, symbol, **kwargs):
        
        params = {}
        params["symbol"] = symbol
        
        # Define a set of valid optional parameters
        valid_options = {"limit", "idLessThan", "startTime", "endTime"}
        
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(GET, SPOT_MARKET_V2_URL + "/fills-history", params)
    
    # ########################################
    # ################ SPOT TRADE ############
    # ########################################
    
    def spot_place_order(self, **kwargs):
        
        # List of required parameters
        required_params = ["symbol", "side", "orderType", "force", "size"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params}
        
        # Define valid optional parameters
        valid_options = {
            "price", "clientOid", "triggerPrice", "tpslType", "requestTime",
            "receiveWindow", "stpMode", "presetTakeProfitPrice",
            "executeTakeProfitPrice", "presetStopLossPrice", "executeStopLossPrice"
        }
        
        # Add optional parameters to params
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(POST, SPOT_TRADE_V2_URL + "/place-order", params)
    
    def spot_cancel_replace_order(self, **kwargs):
                
        # List of required parameters
        required_params = ["symbol", "price", "size"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params}
        
        # Define valid optional parameters
        valid_options = {
            "clientOid", "orderId", "newClientOid", "presetTakeProfitPrice",
            "executeTakeProfitPrice", "presetStopLossPrice", "executeStopLossPrice"
        }
        
        # Check orderId and clientOid
        orderId = kwargs.get("orderId")
        clientOid = kwargs.get("clientOid")
        
        if orderId or clientOid:
            pass
        else:
            raise ValueError("Either 'orderId' or 'clientOid' is required.")
        
        # Add optional parameters to params
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(POST, SPOT_TRADE_V2_URL + "/cancel-replace-order", params)
    
    def spot_cancel_order(self, symbol, **kwargs):
        
        params = {}
        params["symbol"] = symbol
        
        # Define a set of valid optional parameters
        valid_options = {"tpslType", "orderId", "clientOid"}
        
        # Check orderId and clientOid
        orderId = kwargs.get("orderId")
        clientOid = kwargs.pgetop("clientOid")
        
        if orderId or clientOid:
            pass
        else:
            raise ValueError("Either 'orderId' or 'clientOid' is required.")
        
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(GET, SPOT_TRADE_V2_URL + "/cancel-order", params)
    
    def spot_batch_place_order(self, **kwargs):
                
        # List of required parameters
        required_params = ["orderList", "side", "orderType", "force", "size"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params}
        
        # Define valid optional parameters
        valid_options = {
            "symbol", "batchMode", "price", "clientOid", "stpMode", "presetTakeProfitPrice",
            "executeTakeProfitPrice", "presetStopLossPrice", "executeStopLossPrice"
        }
        
        # Add optional parameters to params
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(POST, SPOT_TRADE_V2_URL + "/batch-orders", params)
    
    def spot_batch_cancel_replace_order(self, **kwargs):
                
        # List of required parameters
        required_params = ["orderList", "symbol", "price", "size"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params}
        
        # Define valid optional parameters
        valid_options = {
            "clientOid", "orderId", "newClientOid", "presetTakeProfitPrice",
            "executeTakeProfitPrice", "presetStopLossPrice", "executeStopLossPrice"
        }
        
        # Check orderId and clientOid
        orderId = kwargs.get("orderId")
        clientOid = kwargs.get("clientOid")
        
        if orderId or clientOid:
            pass
        else:
            raise ValueError("Either 'orderId' or 'clientOid' is required.")
        
        # Add optional parameters to params
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(POST, SPOT_TRADE_V2_URL + "/batch-cancel-replace-order", params)
    
    def spot_batch_cancel_order(self, orderList, **kwargs):
        
        params = {}
        params["orderList"] = orderList
        
        # Define a set of valid optional parameters
        valid_options = {"symbol", "batchMode", "orderId", "clientOid"}
        
        # Check orderId and clientOid
        orderId = kwargs.get("orderId")
        clientOid = kwargs.get("clientOid")
        
        if orderId or clientOid:
            pass
        else:
            raise ValueError("Either 'orderId' or 'clientOid' is required.")
        
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(GET, SPOT_TRADE_V2_URL + "/batch-cancel-order", params)
    
    def spot_cancel_order_symbol(self, symbol):
        
        params = {}
        params["symbol"] = symbol
        
        return self._request(GET, SPOT_TRADE_V2_URL + "/cancel-symbol-order", params)
    
    def spot_order_info(self, **kwargs):
        
        params = {}
        
        # Define a set of valid optional parameters
        valid_options = {"orderId", "clientOid", "requestTime", "receiveWindow"}
        
        # Check orderId and clientOid
        orderId = kwargs.get("orderId")
        clientOid = kwargs.get("clientOid")
        
        if orderId or clientOid:
            pass
        else:
            raise ValueError("Either 'orderId' or 'clientOid' is required.")
        
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(GET, SPOT_TRADE_V2_URL + "/orderInfo", params)
    
    def spot_current_order(self, **kwargs):
        
        params = {}
        
        # Define a set of valid optional parameters
        valid_options = {
            "symbol", "startTime", "endTime", "idLessThan", "limit",
            "orderId", "tpslType", "requestTime", "receiveWindow",
        }
        
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(GET, SPOT_TRADE_V2_URL + "/unfilled-orders", params)
    
    def spot_history_order(self, **kwargs):
        
        params = {}
        
        # Define a set of valid optional parameters
        valid_options = {
            "symbol", "startTime", "endTime", "idLessThan", "limit",
            "orderId", "tpslType", "requestTime", "receiveWindow",
        }
        
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(GET, SPOT_TRADE_V2_URL + "/history-orders", params)
    
    def spot_fills(self, symbol, **kwargs):
        
        params = {}
        params["symbol"] = symbol
        
        # Define a set of valid optional parameters
        valid_options = {"orderId", "startTime", "endTime", "limit", "idLessThan"}
        
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(GET, SPOT_TRADE_V2_URL + "/fills", params)
    
    # ########################################
    # ################ SPOT TRIGGER ##########
    # ########################################
    
    def spot_place_plan_order(self, **kwargs):
        
        # List of required parameters
        required_params = ["symbol", "side", "triggerPrice", "orderType", "size", "triggerType"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params}
        
        # Define valid optional parameters
        valid_options = {
            "executePrice", "planType", "clientOid", "force", "stpMode"
        }
        
        # Add optional parameters to params
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(POST, SPOT_TRADE_V2_URL + "/place-plan-order", params)
        
    def spot_modify_plan_order(self, **kwargs):
        
        # List of required parameters
        required_params = ["triggerPrice", "orderType", "size"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params}
        
        # Define valid optional parameters
        valid_options = {
            "orderId", "clientOid", "executePrice"
        }
        
        # Check orderId and clientOid
        orderId = kwargs.get("orderId")
        clientOid = kwargs.get("clientOid")
        
        if orderId or clientOid:
            pass
        else:
            raise ValueError("Either 'orderId' or 'clientOid' is required.")
        
        # Add optional parameters to params
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(POST, SPOT_TRADE_V2_URL + "/modify-plan-order", params)
    
    def spot_cancel_plan_order(self, orderId=None, clientOid=None):
        
        if orderId or clientOid:
            params = {}
            if orderId:
                params["orderId"] = orderId
            if clientOid:
                params["clientOid"] = clientOid
        else:
            raise ValueError("Either 'orderId' or 'clientOid' is required.")
        
        return self._request(POST, SPOT_TRADE_V2_URL + "/cancel-plan-order", params)
    
    def spot_get_current_plan_orders(self, symbol, **kwargs):
        
        params = {}
        params["symbol"] = symbol
        
        # Define a set of valid optional parameters
        valid_options = {"limit", "idLessThan", "startTime", "endTime"}
        
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(GET, SPOT_TRADE_V2_URL + "/current-plan-order", params)  
    
    def spot_get_plan_sub_order(self, planOrderId):
        
        params = {}
        params["planOrderId"] = planOrderId
        
        return self._request(GET, SPOT_TRADE_V2_URL + "/plan-sub-order", params)  
    
    def spot_get_history_plan_orders(self, limit=None, **kwargs):
        
        # List of required parameters
        required_params = ["symbol", "startTime", "endTime"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params} 
        
        if limit:
            params["limit"] = limit
            
        return self._request(GET, SPOT_TRADE_V2_URL + "/history-plan-order", params)  
    
    def spot_batch_cancel_plan_order(self, symbolList=None):
        
        if symbolList:
            params = {}
            params["symbolList"] = symbolList
            return self._request(POST, SPOT_TRADE_V2_URL + "/batch-cancel-plan-order", params)
        else:
            return self._request(POST, SPOT_TRADE_V2_URL + "/batch-cancel-plan-order")
        
    # ########################################
    # ################ SPOT ACCOUNT ##########
    # ########################################    
    
    def spot_get_account_info(self):
        
        return self._request(GET, SPOT_ACCOUNT_V2_URL + "/info")
    
    def spot_get_account_assets(self, coin=None, assetType=None):
        
        if coin or assetType:
            params = {}
            if coin:
                params["coin"] = coin
            if assetType:
                params["assetType"] = assetType
            return self._request(GET, SPOT_ACCOUNT_V2_URL + "/assets", params)
        else:
            return self._request(GET, SPOT_ACCOUNT_V2_URL + "/assets")
        
    def spot_get_sub_account_assets(self):
    
        return self._request(GET, SPOT_ACCOUNT_V2_URL + "/subaccount-assets")
    
    def spot_modify_deposit_account(self, accountType, coin):
        
        params = {}
        params["accountType"] = accountType
        params["coin"] = coin
        
        return self._request(POST, SPOT_ACCOUNT_V2_URL + "/modify-deposit-account", params)
    
    def spot_get_account_bills(self, coin=None, groupType=None):
        
        if coin or groupType:
            params = {}
            if coin:
                params["coin"] = coin
            if groupType:
                params["groupType"] = groupType
            return self._request(GET, SPOT_ACCOUNT_V2_URL + "/bills", params)
        else:
            return self._request(GET, SPOT_ACCOUNT_V2_URL + "/bills")   
        
    def spot_transfer(self, clientOid=None, **kwargs):
        
        # List of required parameters
        required_params = ["fromType", "toType", "amount", "coin", "symbol"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params} 
        
        if clientOid:
            params["clientOid"] = clientOid
            
        return self._request(GET, SPOT_WALLET_V2_URL + "/transfer", params)
    
    def spot_get_transferable_coin_list(self, fromType, toType):
        
        params = {}
        params["fromType"] = fromType
        params["toType"] = toType
        
        return self._request(GET, SPOT_WALLET_V2_URL + "/transfer-coin-info", params)
    
    def spot_sub_transfer(self, **kwargs):
        
        # List of required parameters
        required_params = ["fromType", "toType", "amount", "coin", "fromUserId", "toUserId"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params}
        
        # Define valid optional parameters
        valid_options = {
            "symbol", "clientOid"
        }
        
        # Add optional parameters to params
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(POST, SPOT_WALLET_V2_URL + "/subaccount-transfer", params)  
    
    def spot_withdraw(self, **kwargs):
        
        # List of required parameters
        required_params = ["coin", "transferType", "address", "size"]
        
        # Check for required parameters and raise an error if any are missing
        for param in required_params:
            if param not in kwargs:
                raise ValueError(f"The '{param}' parameter is required.")      

        # Start building the params dictionary with required parameters
        params = {param: kwargs[param] for param in required_params}
        
        # Define valid optional parameters
        valid_options = {
            "chain", "innerToType", "areaCode", "tag", "remark", "clientOid"
        }
        
        # Add optional parameters to params
        for key, value in kwargs.items():
            if key in valid_options and value:
                params[key] = value
                
        return self._request(POST, SPOT_WALLET_V2_URL + "/withdrawal", params)  
            
                 
          