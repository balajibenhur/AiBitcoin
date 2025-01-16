import json
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def create_transaction(sender_key, recipient, amount, sender_private_key):
    transaction = {
        "sender": sender_key,
        "recipient": recipient,
        "amount": amount,
    }
    transaction_bytes = json.dumps(transaction).encode()

    signature = sender_private_key.sign(
        transaction_bytes,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

    transaction["signature"] = signature.hex()
    return transaction

