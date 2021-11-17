import looker_sdk
from home.models import Post

def get_json(slug):
    sdk = looker_sdk.init31()
    me = sdk.me()
    tile = sdk.query_for_slug(slug)
    tile_query = tile.id
    result = sdk.run_query(query_id=tile_query, result_format="json", limit=10)
    print(result)
    return result


#'pRbCV6jUJJLZRcrwHAZXAq'