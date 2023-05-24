import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/minmax')
def min_max_sum():  # put application's code here
    arr = request.json['n']
    sorted_arr = sorted(arr)
    min_sum = sum(sorted_arr[:-1])
    max_sum = sum(sorted_arr[1:])
    response = {
        "Min Sum": min_sum,
        "Max Sum": max_sum,
    }
    return response


if __name__ == '__main__':
    app.run()
