import flask
import json



app = flask.Flask(__name__)



@app.route('/')
def index():
    print("here")
    
   
    #req = flask.request.args.get('req', '')

    return flask.render_template('index.html', wasm_data=open('wasm/original.wasm.base64', 'r').read(), )


app.run(host="0.0.0.0", port=5000, debug=True)