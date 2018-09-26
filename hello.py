def app(env, start_resp):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
        ]
    body = []
    start_resp(status, headers)
    return body
