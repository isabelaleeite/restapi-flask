from application import create_app
import os


if os.getenv("FLASK_ENV") == "development":
    app = create_app('config.DevConfig')
else:
    app = create_app('config.ProdConfig')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host='0.0.0.0', port=port)
