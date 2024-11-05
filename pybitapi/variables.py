# Methods
GET = "GET"
POST = "POST"

# Types
COMMON = ""
SPOT = "spot"
MIX = "mix"
BROKER = "broker"
MARGIN = "margin"
COPY = "copy"
EARN = "earn"

# CATEGORIES
PUBLIC = "public"
MARKET = "market"
TRADE = "trade"
ACCOUNT = "account"
WALLET = "wallet"
INST_LOAN = "ins-loan"
ORDER = "order"
POSITION = "position"
MANAGE = "manage"
CURRENCIES = "currencies"
CROSSED = "crossed"
CROSSED_ACCOUNT = "crossed/account"
SPOT_TRADER = "spot-trader"
SPOT_FOLLOWER = "spot-follower"
MIX_TRADER = "mix-trader"
MIX_FOLLOWER = "mix-follower"
SAVING = "saving"
SHARKFIN = "sharkfin"
LOAN = "loan"


# Base Url and version
API_URL = 'https://api.bitget.com'
API_VERSION = "/api/v2/"

# Header
CONTENT_TYPE = 'Content-Type'
ACCESS_KEY = 'ACCESS-KEY'
ACCESS_SIGN = 'ACCESS-SIGN'
ACCESS_TIMESTAMP = 'ACCESS-TIMESTAMP'
ACCESS_PASSPHRASE = 'ACCESS-PASSPHRASE'
APPLICATION_JSON = 'application/json'
LOCALE = "locale"
EN = "en-US"

# ########################################
# ##############【public url】#############
# ########################################

PUBLIC_V2_URL = '/api/v2/public'

# ########################################
# ##############【spot url】###############
# ########################################

SPOT_PUBLIC_V2_URL = '/api/v2/spot/public'
SPOT_MARKET_V2_URL = '/api/v2/spot/market'
SPOT_TRADE_V2_URL = '/api/v2/spot/trade'
SPOT_ACCOUNT_V2_URL = '/api/v2/spot/account'
SPOT_WALLET_V2_URL = '/api/v2/spot/wallet'
SPOT_INST_LOAN_V2_URL = '/api/v2/spot/ins-loan'

# ########################################
# ##############【mix url】################
# ########################################

MIX_MARKET_V2_URL = '/api/v2/mix/market'
MIX_ACCOUNT_V2_URL = '/api/v2/mix/account'
MIX_TRADE_V2_URL = '/api/v2/mix/order'

# ########################################
# ##############【broker url】#############
# ########################################

BROKER_ACCOUNT_V2_URL = '/api/v2/broker/account'
BROKER_MANAGE_V2_URL = '/api/v2/broker/manage'

# ########################################
# ##############【margin url】#############
# ########################################

MARGIN_CURRENCIES_V2_URL = '/api/v2/margin/currencies'
MARGIN_CROSSED_V2_URL = '/api/v2/margin/crossed'
MARGIN_ACCOUNT_CROSSED_V2_URL = '/api/v2/margin/crossed/account'

# ########################################
# ##############【copy url】###############
# ########################################

COPY_SPOT_TRADER_V2_URL = '/api/v2/copy/spot-trader'
COPY_SPOT_FOLLOWER_V2_URL = '/api/v2/copy/spot-follower'
COPY_MIX_TRADER_V2_URL = '/api/v2/copy/mix-trader'
COPY_mix_FOLLOWER_V2_URL = '/api/v2/copy/mix-follower'

# ########################################
# ##############【earn url】###############
# ########################################

EARN_SAVING_V2_URL = '/api/v2/earn/savings'
EARN_ACCOUNT_V2_URL = '/api/v2/earn/account'
EARN_SHARKFIN_V2_URL = '/api/v2/earn/sharkfin'
EARN_LOAN_V2_URL = '/api/v2/earn/loan'