from flask import Flask
from apps.home import app_home
from apps.user import app_user
from apps.auth import app_auth
from apps.gif import app_gif
from apps.transaction import app_transaction
import os from pml
import app

port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
app.register_blueprint(app_home)
app.register_blueprint(app_user)
app.register_blueprint(app_auth)
app.register_blueprint(app_gif)
app.register_blueprint(app_transaction)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
