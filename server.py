import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/logicbuilder/api/instagram-data1'

mcp = FastMCP('instagram-data1')

@mcp.tool()
def hashtag_feed_v2(hashtag: Annotated[str, Field(description='Instagram hashtag Values accepted: summer')],
                    end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here next_max_id value that you have received in previous request response.')] = None) -> dict: 
    '''Get hashtag post feed V2'''
    url = 'https://instagram-data1.p.rapidapi.com/hashtag/feed/v2'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hashtag': hashtag,
        'end_cursor': end_cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hashtag_info(hashtag: Annotated[str, Field(description='Instagram hashtag Values accepted: summer')]) -> dict: 
    '''Get hashtag metadata, top post, total posts and etc'''
    url = 'https://instagram-data1.p.rapidapi.com/hashtag/info'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hashtag': hashtag,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hashtag_reels_feed(hashtag: Annotated[str, Field(description='Instagram hashtag Values accepted: summer')],
                       end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here end_cursor value that you have received in previous request response.')] = None) -> dict: 
    '''Get hashtag reels feed'''
    url = 'https://instagram-data1.p.rapidapi.com/hashtag/feed/reels'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hashtag': hashtag,
        'end_cursor': end_cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hashtag_feed(hashtag: Annotated[str, Field(description='Instagram hashtag Values accepted: summer')],
                 end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here end_cursor value that you have received in previous request response.')] = None) -> dict: 
    '''Get hashtag post feed'''
    url = 'https://instagram-data1.p.rapidapi.com/hashtag/feed'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hashtag': hashtag,
        'end_cursor': end_cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_stories(location_ids: Annotated[str, Field(description='Location ids should specified in the following format: LOCATION_ID,LOCATION_ID,... Location ids can be found by using /location/search endpoint For example: 2082352,75929182,6811413,130521400908152,59736,1161978,221177873')]) -> dict: 
    '''Get location user stories by using set of location ids values. **Location ids can be found by using /location/search endpoint**'''
    url = 'https://instagram-data1.p.rapidapi.com/location/stories'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_ids': location_ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_search(location: Annotated[str, Field(description='Location name, for example: new york')]) -> dict: 
    '''Get locations metadata (id and etc)'''
    url = 'https://instagram-data1.p.rapidapi.com/location/search'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_feed(location_id: Annotated[Union[int, float], Field(description='Location ID For example in this link https://www.instagram.com/explore/locations/213385402/london-united-kingdom/ the location_id value will be 213385402 Values accepted: 213385402 Default: 213385402')],
                  end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here end_cursor value that you have received in previous request response.')] = None) -> dict: 
    '''Get location post feed'''
    url = 'https://instagram-data1.p.rapidapi.com/location/feed'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location_id': location_id,
        'end_cursor': end_cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def post_comments_v2(post: Annotated[str, Field(description='Post example url: https://www.instagram.com/p/CAVeEm1gDh2/')],
                     next_min_id: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here next_min_id value that you have received in previous request response.')] = None) -> dict: 
    '''Get post comments V2 - more accurate data **NOTE:** Profile should be public(not private)'''
    url = 'https://instagram-data1.p.rapidapi.com/comments/v2'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'post': post,
        'next_min_id': next_min_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def post_metadata(post: Annotated[str, Field(description='Instagram post url. Two url formats are accepted: https://www.instagram.com/p/CG5a3RcDb8X/ CG5a3RcDb8X')]) -> dict: 
    '''Get post metadata **NOTE:** Profile should be public(not private)'''
    url = 'https://instagram-data1.p.rapidapi.com/post/info'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'post': post,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def post_comments(post: Annotated[str, Field(description='Post Values accepted: CAVeEm1gDh2 https://www.instagram.com/p/CAVeEm1gDh2/')],
                  end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here end_cursor value that you have received in previous request response.')] = None) -> dict: 
    '''Get post comments **NOTE:** Profile should be public(not private)'''
    url = 'https://instagram-data1.p.rapidapi.com/comments'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'post': post,
        'end_cursor': end_cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def post_likers(post: Annotated[str, Field(description='Post Values accepted: CAVeEm1gDh2 https://www.instagram.com/p/CAVeEm1gDh2/')],
                end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here end_cursor value that you have received in previous request response.')] = None) -> dict: 
    '''Get users that liked specific post **NOTE:** Profile should be public(not private)'''
    url = 'https://instagram-data1.p.rapidapi.com/likers'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'post': post,
        'end_cursor': end_cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_information(username: Annotated[str, Field(description='Instagram username')]) -> dict: 
    '''Get user information(followers, followings and etc)'''
    url = 'https://instagram-data1.p.rapidapi.com/user/info'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_information_by_user_id(user_id: Annotated[Union[int, float], Field(description='Instagram username Default: 25025320')]) -> dict: 
    '''Get user information(followers, followings and etc) by using user id (numbers)'''
    url = 'https://instagram-data1.p.rapidapi.com/user/info/id'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user_id': user_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_stories(username: Annotated[Union[str, None], Field(description='Instagram username')] = None,
                 user_id: Annotated[Union[str, None], Field(description='By using user_id instead of the username your request will be executed much faster')] = None) -> dict: 
    '''Retrieve active user stories **NOTE:** By using **user_id** instead of the username your request will be executed much faster'''
    url = 'https://instagram-data1.p.rapidapi.com/user/stories'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'user_id': user_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_reels_feed(username: Annotated[Union[str, None], Field(description='Instagram username')] = None,
                    limit: Annotated[Union[int, float, None], Field(description='Number of items(posts) to return Default value: 25 Limit: 150 Default: 25')] = None,
                    end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here end_cursor value that you have received in previous request response.')] = None,
                    user_id: Annotated[Union[str, None], Field(description='By using user_id instead of the username your request will be executed much faster')] = None) -> dict: 
    '''Get user reels feed **NOTE:** By using **user_id** instead of the username your request will be executed much faster'''
    url = 'https://instagram-data1.p.rapidapi.com/user/reels'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'limit': limit,
        'end_cursor': end_cursor,
        'user_id': user_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_contact_details_email_phone_and_etc(username: Annotated[Union[str, None], Field(description='Instagram username')] = None,
                                             user_id: Annotated[Union[str, None], Field(description='By using user_id instead of the username your request will be executed much faster')] = None) -> dict: 
    '''Get user contact details such as email, phone and etc **NOTE:** By using **user_id** instead of the username your request will be executed much faster **NOTE: the output will include email, phone only IF THESE DATA IS AVAILABLE in IG**'''
    url = 'https://instagram-data1.p.rapidapi.com/user/contacts'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'user_id': user_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_followings(username: Annotated[Union[str, None], Field(description='Instagram username. Values accepted: instagram https://www.instagram.com/instagram/')] = None,
                    end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here end_cursor value that you have received in previous request response.')] = None,
                    user_id: Annotated[Union[str, None], Field(description='By using user_id instead of the username your request will be executed much faster')] = None) -> dict: 
    '''Get user followings **NOTE:** By using **user_id** instead of the username your request will be executed much faster **NOTE:** Profile should be public(not private)'''
    url = 'https://instagram-data1.p.rapidapi.com/followings'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'end_cursor': end_cursor,
        'user_id': user_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_followers(username: Annotated[Union[str, None], Field(description='Instagram username. Values accepted: instagram https://www.instagram.com/instagram/')] = None,
                   end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here end_cursor value that you have received in previous request response.')] = None,
                   user_id: Annotated[Union[str, None], Field(description='By using user_id instead of the username your request will be executed much faster')] = None) -> dict: 
    '''Get user followers **NOTE:** By using **user_id** instead of the username your request will be executed much faster **NOTE:** Profile should be public(not private)'''
    url = 'https://instagram-data1.p.rapidapi.com/followers'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'end_cursor': end_cursor,
        'user_id': user_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_feed(username: Annotated[Union[str, None], Field(description='Instagram username. Values accepted: instagram https://www.instagram.com/instagram/')] = None,
              end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here end_cursor value that you have received in previous request response.')] = None,
              limit: Annotated[Union[int, float, None], Field(description='Limit number of posts to output. Min 1 Max 50 Default: 0')] = None,
              user_id: Annotated[Union[str, None], Field(description='By using user_id instead of the username your request will be executed much faster')] = None) -> dict: 
    '''Get user post feed **NOTE:** By using **user_id** instead of the username your request will be executed much faster **NOTE:** Profile should be public(not private)'''
    url = 'https://instagram-data1.p.rapidapi.com/user/feed'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'end_cursor': end_cursor,
        'limit': limit,
        'user_id': user_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_story_highlight_metadata(url: Annotated[str, Field(description='Direct url to a user story highlight Example: https://www.instagram.com/stories/highlights/17866745050538306/')]) -> dict: 
    '''Get user story highlight metadata from a direct url to a story'''
    url = 'https://instagram-data1.p.rapidapi.com/user/stories/highlights'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_highlight_reels_feed(username: Annotated[Union[str, None], Field(description='Username For example: dhairiusnyc')] = None,
                              user_id: Annotated[Union[str, None], Field(description='By using user_id instead of the username your request will be executed much faster')] = None) -> dict: 
    '''Get user highlight reels feed **NOTE:** By using **user_id** instead of the username your request will be executed much faster **NOTE:** Profile should be public(not private)'''
    url = 'https://instagram-data1.p.rapidapi.com/user/highlight/reels'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'user_id': user_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_feed_v2(username: Annotated[str, Field(description='Instagram username. Values accepted: instagram https://www.instagram.com/instagram/')],
                 end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here ** next_max_id** value that you have received in previous request response.')] = None,
                 limit: Annotated[Union[int, float, None], Field(description='Limit number of posts to output. Min 1 Max 30 Default: 0')] = None) -> dict: 
    '''Get user post feed v2 **NOTE:** Profile should be public(not private)'''
    url = 'https://instagram-data1.p.rapidapi.com/user/feed/v2'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'end_cursor': end_cursor,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_guides_feed(username: Annotated[Union[str, None], Field(description='Instagram username')] = None,
                     max_id: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here next_max_id value that you have received in previous request response.')] = None,
                     user_id: Annotated[Union[str, None], Field(description='By using user_id instead of the username your request will be executed much faster')] = None) -> dict: 
    '''Get user guides feed **NOTE:** Profile should be public(not private) **NOTE:** By using **user_id** instead of the username your request will be executed much faster'''
    url = 'https://instagram-data1.p.rapidapi.com/user/guides/feed'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'max_id': max_id,
        'user_id': user_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_tagged_feed(username: Annotated[Union[str, None], Field(description='Instagram username')] = None,
                     end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here end_cursor value that you have received in previous request response.')] = None,
                     user_id: Annotated[Union[str, None], Field(description='By using user_id instead of the username your request will be executed much faster')] = None) -> dict: 
    '''Get user tagged feed, post where user was tagged **NOTE:** Profile should be public(not private) **NOTE:** By using **user_id** instead of the username your request will be executed much faster'''
    url = 'https://instagram-data1.p.rapidapi.com/user/tagged/feed'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'end_cursor': end_cursor,
        'user_id': user_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_search(keyword: Annotated[str, Field(description='Any keyword')]) -> dict: 
    '''Search for a users by using keyword'''
    url = 'https://instagram-data1.p.rapidapi.com/user/search'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hashtag_search(keyword: Annotated[str, Field(description='Any keyword')]) -> dict: 
    '''Search for a hashtags by using keyword'''
    url = 'https://instagram-data1.p.rapidapi.com/hashtag/search'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def audio_feed(audio_id: Annotated[str, Field(description='Audio id For example: https://www.instagram.com/reels/audio/921447351682109/ 921447351682109 - will be the audio_id')],
               end_cursor: Annotated[Union[str, None], Field(description='Pagination cursor. To get next batch of data, paste here end_cursor value that you have received in previous request response.')] = None) -> dict: 
    '''Get audio post feed'''
    url = 'https://instagram-data1.p.rapidapi.com/audio/feed'
    headers = {'x-rapidapi-host': 'instagram-data1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'audio_id': audio_id,
        'end_cursor': end_cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
