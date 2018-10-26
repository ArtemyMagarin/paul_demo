from bottle import Bottle, run, get, post, request, template

app = Bottle()

@app.get('/')
def index():
    return template('index.html', data={})
    
@app.post('/')
def sum():
	a = request.forms.get('a')
	b = request.forms.get('b')

	try:
		s = int(a) + int(b)
	except Exception:
		s = 'error'

	return template('index.html', data={ 'answer': s, 'a': a, 'b': b })

run(app, host='127.0.0.1', port=8080)