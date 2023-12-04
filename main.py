from flask import Flask,render_template, request
import test as d
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/rodada', methods=['get', 'post'])
def rodada():
    if request.method == 'POST':
        numero_rodada = int(request.form.get('numero_rodada'))-1
        if 38 >= numero_rodada > 0:
            return d.rod(int(numero_rodada))
        return d.rod(0)
    
if __name__ == '__main__':
    app.run(debug=True)
