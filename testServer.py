import web

urls = (
    '/wx', 'Handle',
)

class Handle(object):
    def GET(self):
        return "hello, this is python handle view"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()