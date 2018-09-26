def app(env, start_resp):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
        ]
    body = [i for i in env[QUERY_STRING].split('&')]
    start_resp(status, headers)
    return body
