# AiBitcoin: Detailed Usage Examples

This document provides step-by-step instructions for using AiBitcoin, including creating wallets, conducting transactions, deploying nodes, and validating the blockchain.

---

## **1. Generating a Wallet**
### Steps:
1. Run the wallet generation script:
   ```bash
   python scripts/generate_keys.py
Specify a directory to save the keys (or press Enter for the default keys/ directory).
Verify the generated files in the specified directory:

    ls keys/
    private_key.pem
    public_key.pem

Using the Wallet in Code:

from src.wallet.wallet import Wallet
wallet = Wallet()
print("Public Key:", wallet.public_key)

2. Conducting Transactions
Create a Transaction:

    Import the transactions.py module:

from src.wallet.transactions import create_transaction

Use the function to create a transaction:

transaction = create_transaction(sender_public_key, recipient_public_key, amount, sender_private_key)

Broadcast the transaction (simulated example):

    from src.network.peer_to_peer import broadcast_transaction
    broadcast_transaction(transaction)

3. Starting a Node

    Run the deployment script:

python scripts/deploy_node.py

Test if the node is running:

    curl http://localhost:5000/blockchain

4. Verifying the Blockchain
Using Code:

    Import the blockchain.py module:

from src.blockchain.blockchain import Blockchain
blockchain = Blockchain()

Validate the blockchain:

print("Is blockchain valid?", blockchain.is_valid_chain())

Add a block to the chain:

    blockchain.add_block("Sample Transaction Data", proof)


