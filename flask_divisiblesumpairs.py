import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def divisible_sum_pairs():  # put application's code here
    n= request.json['n']
    k = request.json['k']
    ar = request.json['ar']

    count = 0
    for i in range(0,len(ar), 1):
        for j in range(i + 1, len(ar), 1):
            if (ar[i] + ar[j]) % k == 0:
                count += 1

    response = {"response": count}
    return response


if __name__ == '__main__':
    app.run()
