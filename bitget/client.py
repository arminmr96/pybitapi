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
        
        if coin is not None:
            params = {}
            params["coin"] = coin
            return self._request(GET, SPOT_MARKET_V2_URL + "/coins", params)
        else:
            return self._request(GET, SPOT_MARKET_V2_URL + "/coins")
        
    def spot_symbol_info(self, symbol=None):
        
        if symbol is not None:
            params = {}
            params["symbol"] = symbol
            return self._request(GET, SPOT_MARKET_V2_URL + "/symbols", params)
        else:
            return self._request(GET, SPOT_MARKET_V2_URL + "/symbols")
    
    def spot_vip_fee_rate(self):
        
        return self._request(GET, SPOT_MARKET_V2_URL + "/vip-fee-rate")
    
    def spot_ticker_info(self, symbol=None):
        
        if symbol is not None:
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
            if key in valid_options and value is not None:
                params[key] = value
                
        return self._request(GET, SPOT_MARKET_V2_URL + "/merge-depth", params)
    
    def spot_orderbook_depth(self, symbol, **kwargs):
        
        params = {}
        params["symbol"] = symbol
        
        # Define a set of valid optional parameters
        valid_options = {"type", "limit"}
        
        for key, value in kwargs.items():
            if key in valid_options and value is not None:
                params[key] = value
                
        return self._request(GET, SPOT_MARKET_V2_URL + "/orderbook", params)
    
    def spot_candlestick_data(self, symbol, granularity, **kwargs):
        
        params = {}
        params["symbol"] = symbol
        params["granularity"] = granularity
        
        # Define a set of valid optional parameters
        valid_options = {"startTime", "endTime", "limit"}
        
        for key, value in kwargs.items():
            if key in valid_options and value is not None:
                params[key] = value
                
        return self._request(GET, SPOT_MARKET_V2_URL + "/candles", params)
    
    def spot_history_candlestick_data(self, symbol, granularity, endTime, limit=None):
        
        params = {}
        params["symbol"] = symbol
        params["granularity"] = granularity
        params["endTime"] = endTime
        if limit is not None:
            params["limit"] = limit
            
        return self._request(GET, SPOT_MARKET_V2_URL + "/candles", params)
    
    def spot_recent_trades(self, symbol, limit=None):
        
        params = {}
        params["symbol"] = symbol
        if limit is not None:
            params["limit"] = limit
            
        return self._request(GET, SPOT_MARKET_V2_URL + "/fills", params)
    
    def spot_market_trades(self, symbol, **kwargs):
        
        params = {}
        params["symbol"] = symbol
        
        # Define a set of valid optional parameters
        valid_options = {"limit", "idLessThan", "startTime", "endTime"}
        
        for key, value in kwargs.items():
            if key in valid_options and value is not None:
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
            if key in valid_options and value is not None:
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
        
        # Add optional parameters to params
        for key, value in kwargs.items():
            if key in valid_options and value is not None:
                params[key] = value
                
        return self._request(POST, SPOT_TRADE_V2_URL + "/cancel-replace-order", params)
    
    def spot_cancel_order(self, symbol, **kwargs):
        
        params = {}
        params["symbol"] = symbol
        
        # Define a set of valid optional parameters
        valid_options = {"tpslType", "orderId", "clientOid"}
        
        for key, value in kwargs.items():
            if key in valid_options and value is not None:
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
            if key in valid_options and value is not None:
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
        
        # Add optional parameters to params
        for key, value in kwargs.items():
            if key in valid_options and value is not None:
                params[key] = value
                
        return self._request(POST, SPOT_TRADE_V2_URL + "/batch-cancel-replace-order", params)
    
    def spot_batch_cancel_order(self, orderList, **kwargs):
        
        params = {}
        params["orderList"] = orderList
        
        # Define a set of valid optional parameters
        valid_options = {"symbol", "batchMode", "orderId", "clientOid"}
        
        for key, value in kwargs.items():
            if key in valid_options and value is not None:
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
        
        for key, value in kwargs.items():
            if key in valid_options and value is not None:
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
            if key in valid_options and value is not None:
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
            if key in valid_options and value is not None:
                params[key] = value
                
        return self._request(GET, SPOT_TRADE_V2_URL + "/history-orders", params)
    
    def spot_fills(self, symbol, **kwargs):
        
        params = {}
        params["symbol"] = symbol
        
        # Define a set of valid optional parameters
        valid_options = {"orderId", "startTime", "endTime", "limit", "idLessThan"}
        
        for key, value in kwargs.items():
            if key in valid_options and value is not None:
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
            if key in valid_options and value is not None:
                params[key] = value
                
        return self._request(POST, SPOT_TRADE_V2_URL + "/place-plan-order", params)
        