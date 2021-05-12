import requests
from flask import Flask, Response
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)
link = api.parser()
link.add_argument('url', type=str)


@api.route('/api/v1/ping')
class Ping(Resource):

    def post(self):
        args = link.parse_args()
        url = args['url']
        try:
            r = requests.get(
                url=url,
                params=args
            )
            return r.json()
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }


@api.route('/health')
class Health(Resource):

    def get(self):
        return Response("{'Health': 'Healthy'}", status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
