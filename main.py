from flask import Flask, jsonify
from flask_cors import CORS
from utility import leetcode, generate, analyse

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def index():
    return jsonify({
        'message': 'Hello World'
    })
    
@app.route('/profile/<string:username>', methods = ['GET'])
def profile(username):
    details = leetcode.get_leetcode_details_from_username(username)

    if details == None:
        message = "Couldn't fetch details"
    else:
        message = "Details fetched"

        details['matchedUser']['rating'] = details['userContestRanking']['rating']
        details = details['matchedUser']
        
        df = generate.generate_df(details)
        analysis = analyse.analyse(df)

        details = {
            'profile': details['profile'],
            'rating': details['rating'],
            'problems': df['problems'][0],
            'analysis': analysis
        }
    
    response = {
        'message': message,
        'data': details
    }
  
    return jsonify(response)
    
if __name__ == "__main__":
    app.run(debug = True, port = 80)