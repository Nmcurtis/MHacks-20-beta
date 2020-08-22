from aiohttp import web
import app


def main():
    webapp = app.create_app()
    web.run_app(webapp)

main()