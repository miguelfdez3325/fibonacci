from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@app.route('/fibonacci', methods=['GET'])
def calcular_fibonacci():
    try:
        n = int(request.args.get('n'))
        resultado = fibonacci(n)
        return jsonify({'indice': n, 'valor': resultado})
    except ValueError:
        return jsonify({'error': 'El parámetro "n" debe ser un número entero válido.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
