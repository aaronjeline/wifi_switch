#!/usr/bin/python
import web

urls = (
        '/', 'index'
)

app = web.application(urls,globals())

status = False

class index:
    def GET(self):
        return """
        <html>
            <head>
                <title>Light Switch</title>
            </head>

            <body>
                Light Switch Server: </br>
                Current Status: """ + str(status) + """
                </br>
                <form action="/" method="post">
                    <button type="submit">Flip Switch</button>
                </form>
            </body>
        </html>
        """

    def POST(self):
        global status
        status = not status
        return self.GET()

if __name__ == '__main__':
    app.run()
