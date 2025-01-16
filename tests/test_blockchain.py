import unittest
from src.blockchain.blockchain import Blockchain
from src.blockchain.block import Block

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_genesis_block(self):
        self.assertEqual(len(self.blockchain.chain), 1)
        self.assertEqual(self.blockchain.chain[0].index, 0)
        self.assertEqual(self.blockchain.chain[0].previous_hash, "0")

    def test_add_block(self):
        block = Block(index=1, previous_hash=self.blockchain.last_block.hash, transactions=[])
        proof = block.compute_hash()
        self.assertTrue(self.blockchain.add_block(block, proof))

    def test_invalid_block(self):
        block = Block(index=1, previous_hash="wrong_hash", transactions=[])
        proof = block.compute_hash()
        self.assertFalse(self.blockchain.add_block(block, proof))

if __name__ == "__main__":
    unittest.main()
