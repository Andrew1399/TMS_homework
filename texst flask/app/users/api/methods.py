import json

import flask


users_blueprint = flask.Blueprint('users', __name__, url_prefix='/app/users')


@users_blueprint.route('/', methods=['GET'])
def get_users():
    #TODO: Переписать чтобы не было хардкода строки
    # Можно посмотреть решения с помощью стандартного пакета os
    # Или стороннего pathlib
    with open('/Users/boobaleo/Desktop/TeachMeSkills/14 занятие/flask_test_app_2/app/users/mock_data/users.json') as f:
        data = json.load(f)
    return flask.jsonify(data)
