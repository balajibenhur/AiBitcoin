import requests

def broadcast_transaction(transaction):
    peers = ["http://localhost:5000"]
    for peer in peers:
        try:
            response = requests.post(f"{peer}/add_transaction", json=transaction)
            if response.status_code != 200:
                print(f"Failed to broadcast to {peer}")
        except Exception as e:
            print(f"Error broadcasting to {peer}: {e}")

