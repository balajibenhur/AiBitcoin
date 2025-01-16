from src.wallet.wallet import Wallet

def main():
    wallet = Wallet()
    wallet.save_keys()
    print("Keys generated and saved to the keys/ directory.")

if __name__ == "__main__":
    main()
