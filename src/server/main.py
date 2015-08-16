from bottle import Bottle, request

bottle = Bottle()

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

#[{'URL': 'http://example.com/', 'comments': ['a','b','c']},...]
comments = []

@bottle.get('/')
def index():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@bottle.post('/')
def post():
    response = {}
    keys = request.json.keys()
    if 'URL' in keys:
        if request.json['URL']:
            for dict in (item for item in comments if item["URL"] == request.json['URL']):
                response = dict

            if not response:
                response = {'URL': request.json['URL'], 'comments': []}
                comments.append(response)

    if response:
        if 'comment' in keys:
            if request.json['comment']:
                response['comments'].insert(0,request.json['comment'])

    return response


# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'
