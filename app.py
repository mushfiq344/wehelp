from flask import Flask,render_template,url_for,jsonify,request,json
# this is development branch 2
from classes.business import Business

# from dbconnect import connection
app = Flask(__name__)
# @app.route('/register', methods=["GET","POST"])
# def register_page():
#     try:
#         c, conn = connection()
#         return("okay")
#     except Exception as e:
#         return(str(e))

@app.route('/condition', methods=['GET', 'POST'])
def condition():

	condition=Business()

	if request.method=='POST':

		validated = condition.validateCondInputReq(request.json['condition'])

		if validated:
			condition.insertCondition(request.json['condition'])
			response = app.response_class(
				response=json.dumps(request.json['condition']),
				status=200,
				mimetype='application/json'
			)

		else:
			response = app.response_class(
				response="Validation Failed",
				status=400,
				mimetype='application/json'
			)

	if request.method == 'GET':
		condition=Business()
		response = app.response_class(response=json.dumps(condition.getCondition()),
									  status=200,
									  mimetype='application/json')

	return response



@app.route('/user', methods=['GET','PUT'])
def user():
	return "hy"
	# user=Business()
	#
	# if request.method=='PUT':
	#
	# 	validated = user.validateUserPutReq(request.json)
	# 	if validated:
	#
	# 		response = app.response_class(
	# 			response=json.dumps(user.updateUser(request.json)),
	# 			status=200,
	# 			mimetype='application/json'
	# 		)
	# 	else:
	# 		response = app.response_class(
	# 			response="Validation Failed",
	# 			status=400,
	# 			mimetype='application/json'
	# 		)
	#
	#
	# return response

if __name__ == '__main__':
	app.run(debug=True)