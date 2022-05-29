from app.main import create_app
from app.models.base import db
from flask import Blueprint

app = create_app()



if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port, debug=True)
