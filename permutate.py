from flask import Flask, jsonify, request
from itertools import permutations
from waitress import serve

app = Flask(__name__)

@app.route('/permutate', methods=['POST'])
def permutate():
  return get_permutations(request.get_data(as_text=True))

  
def get_permutations(input):
  perms_list = list(permutations(input, len(input)))
  perms = '\n'.join([''.join(perm) for perm in perms_list])
  return perms

if __name__ == "__main__":
    # app.run(debug=False, host='0.0.0.0', port=5001)
    serve(app, host="0.0.0.0", port=8080)
