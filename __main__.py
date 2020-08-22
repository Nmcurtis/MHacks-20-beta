from aiohttp import web
import app

webapp = app.create_app()
web.run_app(webapp)

