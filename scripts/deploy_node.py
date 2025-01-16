from flask import Flask, jsonify
from src.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    chain_data = [vars(block) for block in blockchain.chain]
    return jsonify(chain_data)

if __name__ == "__main__":
    app.run(port=5000)

