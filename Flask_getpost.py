from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

income = [
    {"Description":"salary", "amount":5000}
         ]

@app.route('/income')
def get_incomes():
    return jsonify(income)

# post (works in postman)
@app.route('/income', methods=["POST"])
def add_income():
    income.append(request.get_json())
    return "Created", 201

stock = {
    "fruit":{
              "apple":100,
              "banana":40,
              "cherry":80
            }
         }

# GET (works in postman)
@app.route("/stock")
def get_stock():
    res = make_response(jsonify(stock), 200)
    return res


@app.route("/stock/<collection>")
def get_collection(collection):
    if collection in stock:
        res = make_response(jsonify(stock[collection]), 200)
        return res
    res = make_response(jsonify({"Error":"Not found"}), 404)
    return res

@app.route("/stock/<collection>/<name>")
def get_member(collection, name):
    if collection in stock:
        if name in stock[collection] :
            res = make_response(jsonify(stock[collection][name]), 200)
            return res
        res = make_response(jsonify({"error": "Not Found"}), 200)
        return res
    res = make_response(jsonify({"error": "Not Found"}), 200)
    return res

# Put (to update the collection but it do not replace the apple value)   # request.get_json() accepts the data which you want to put
# @app.route("/stock/<collection>", methods=["PUT"])
# def put_collection(collection):
#     req = request.get_json()
#     if collection in stock:
#         stock[collection] = req
#         res = make_response(jsonify({"msg":"collection created..."}), 200)
#         return res
#     stock[collection] = req
#     res = make_response(jsonify({"msg":"collection created..."}), 200)
#     return res

# PUT (this will replace the apple value)
@app.route("/stock/<collection>", methods=["PUT"])
def put_collection(collection):
    req=request.get_json()
    if collection in stock:
        original = stock[collection]
        for key,value in req.items():
            if key in original:
                original[key]=value
            else:
                original[key]=value
        stock[collection]=req
        res=make_response(jsonify({"msg":"collection updated"}),200)
        return res
    #either create or we need to send error saying record not found for updation
    #stock[collection]=req
    res = make_response(jsonify({"error": "not found"}), 404)
    return res

# Delete collection
# @app.route("/stock/<collection>", methods=["DELETE"])
# def delete_collection(collection):
#     if collection in stock:
#         del stock[collection]
#         res = make_response(jsonify({"msg":"collection Deleted.."}),200)
#         return res
#     else:
#         res = make_response(jsonify({"msg": "collection not present.."}), 204)
#         return res

# delete member
@app.route("/stock/<collection>/<member>", methods=["DELETE"])
def delete_collection(collection, member):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            res = make_response(jsonify({"msg":"collection Deleted.."}), 200)
            return res
        else:
            res = make_response(jsonify({"msg": "member not present.."}), 201)
            return res
    else:
        res = make_response(jsonify({"msg": "collection not present.."}), 205)
        return res


if __name__ == '__main__':
    app.run(debug=True, port=5001)