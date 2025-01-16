import unittest
import os
from src.wallet.wallet import Wallet
from src.wallet.transactions import create_transaction

class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet()

    def test_wallet_creation(self):
        self.assertIsNotNone(self.wallet.private_key)
        self.assertIsNotNone(self.wallet.public_key)

    def test_save_keys(self):
        path = "test_keys/"
        os.makedirs(path, exist_ok=True)
        self.wallet.save_keys(path=path)
        self.assertTrue(os.path.exists(f"{path}private_key.pem"))
        self.assertTrue(os.path.exists(f"{path}public_key.pem"))

        # Cleanup
        os.remove(f"{path}private_key.pem")
        os.remove(f"{path}public_key.pem")
        os.rmdir(path)

class TestTransactions(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet()

    def test_create_transaction(self):
        recipient = "recipient_public_key"
        amount = 100
        transaction = create_transaction(
            sender_key=self.wallet.public_key.public_bytes().hex(),
            recipient=recipient,
            amount=amount,
            sender_private_key=self.wallet.private_key
        )
        self.assertIn("signature", transaction)
        self.assertEqual(transaction["recipient"], recipient)
        self.assertEqual(transaction["amount"], amount)

if __name__ == "__main__":
    unittest.main()
