from flask import Flask, request, jsonify
from AG import algoritmo_genetico
import json
import os


app = Flask(__name__)

with open('componentes2.json', 'r') as json_file:
    componentesJson = json.load(json_file)

@app.route('/api/melhor_configuracao', methods=['POST'])
def melhor_configuracao():
    data = request.json
    componentes = componentesJson
    limite_valor = data.get('limite_valor')
    

    if not componentes or not limite_valor :
        return jsonify({'error': 'Dados incompletos fornecidos'}), 400


    melhor_config, custo_final, pontuacao_final = algoritmo_genetico(
        componentes, limite_valor
    )

    if melhor_config:
        return jsonify({
            'melhor_configuracao': melhor_config,
            'custo_final': custo_final,
            'pontuacao_final': pontuacao_final
        })
    else:
        return jsonify({'message': 'Não foi encontrada uma configuração válida dentro do limite de valor'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)

