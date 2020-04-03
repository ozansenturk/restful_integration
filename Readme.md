Highlights

The application initialization is delayed with factory pattern therefore it 
supports different environments with 'create_app'.

Blueprints reinforces modular and object oriented architecture for high 
cohesive and loose coupled code.

The core part is 'app.api' composed of 'services' and 'utils' modules. Services
provides 'API Integration' whilst 'utils' offers handy functions. Cache feature
in services avoid excessive calls of 'Get Token' service by caching the token 
for along its expiration time. For example, after token retrieved, it is stored
in the cache. Following token calls first check the expiration time and then the cache.
When the token is in the cache and expiration time is still valid, 'Get Token' service
does not make an 'API call' but 'cache read'.

Additionally, request hooking was used to avoid code duplication. For example. Given that 
'post_query' service in services module is the key service which is used for all 
the API calls, 'get_token' service called before each 'post_query' service to inject the 
token into 'post_query' service. This eases debugging and readability. 
 

Setup:

Execute the code below for test coverage:
current coverage is 50%

```python
flask test --coverage
```

Execute the codes below for installment:

```python

python3 -m venv venv
source venv/bin/activate
pip install -r requirements/common.txt
flask run

```


Feel free to reach me for further inquiries. Ozan Senturk (ozan.senturk@gmail.com)
