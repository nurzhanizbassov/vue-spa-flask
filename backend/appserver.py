"""
appserver.py

Creates and application instance and launches the application server.

"""

if __name__ == '__main__':
    from somewebapp_api.application import create_app
    app = create_app()
    app.run()
