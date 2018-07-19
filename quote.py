from flask import Flask,jsonify
from flask import request
import json
import fortune

app = Flask(__name__)
hashSet = set([])

@app.errorhandler(404)
def error(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.route('/quote')
def returnQuote():
    if 'uid' in request.args:
        print hashSet
        uid = request.args['uid']

        while True:
            quote = fortune.get_random_fortune('/Users/luca/Desktop/flask/fortunes')
            uidHash = hash(str(uid)+str(quote))
            print uidHash
            if not uidHash in hashSet:
                print 'uid hash not in hash set'
                break

        hashSet.add(uidHash)

        data = {'quote' : quote}
        return jsonify(data)


if __name__=='__main__':
    app.run(debug=True)
