import flask
import json
import HCaptcha.modules.hsw



app = flask.Flask(__name__)



@app.route('/')
def index():
    print("here")
    
    ua = flask.request.headers.get('ua', '')
    req = flask.request.args.get('req', '')
    href = flask.request.args.get('href', '')
    submit = int(flask.request.args.get('submit', False))
    if submit == 0:
        submit = False
    elif submit == 1:
        submit = True

    return flask.render_template('index.html', wasm_data=open('wasm/original.wasm.base64', 'r').read(), fp_export=
        json.dumps(HCaptcha.modules.hsw.hsw(ua, req, href, submit), indent=4))


app.run(debug=True)