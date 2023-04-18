from .utils import load_json_file

credentials_path = "user_credentials.json"


default_language = "en"
currency = "INR"
credentials_path = "telegram_ecommerce/utils/user_credentials.json"
credentials = load_json_file(credentials_path)
db_credentials = credentials["db_credentials"]
provider_token = credentials["provider_token"]
BAD_RATING = 0
REGULAR_RATING = 5
GOOD_RATING = 10



