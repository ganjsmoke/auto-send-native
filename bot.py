import random
import secrets
from web3 import Web3
from colorama import Fore, Style, init
import time

# Initialize colorama
init(autoreset=True)

def print_header():
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.CYAN + Style.BRIGHT + "Auto Send Native Token".center(50))
    print(Fore.YELLOW + "Supports EVM Chains".center(50))
    print(Fore.GREEN + "Bot created by: https://t.me/airdropwithmeh".center(50))
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    
# Transfer native tokens function
def TransferNative(sender, senderkey, recipient, amount, web3, retries=3):
    for attempt in range(retries):
        try:
            # Estimate gas limit contract
            gas_tx = {
                'chainId': web3.eth.chain_id,
                'from': sender,
                'to': recipient,
                'value': web3.to_wei(amount, 'ether'),
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(sender)
            }
            gasAmount = web3.eth.estimate_gas(gas_tx)

            auto_tx = {
                'chainId': web3.eth.chain_id,
                'from': sender,
                'gas': gasAmount,
                'to': recipient,
                'value': web3.to_wei(amount, 'ether'),
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(sender)
            }

            fixamount = '%.18f' % float(amount)
            # Sign the transaction
            sign_txn = web3.eth.account.sign_transaction(auto_tx, senderkey)
            # Send transaction
            print(Fore.CYAN + f'Processing Send {fixamount} Native To Random New Address : {recipient} ...')
            tx_hash = web3.eth.send_raw_transaction(sign_txn.rawTransaction)

            # Get transaction hash
            txid = str(web3.to_hex(tx_hash))
            transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            print(Fore.GREEN + f'Send {fixamount} Native To Random New Address : {recipient} Success!')
            print(Fore.GREEN + f'TX-ID : {txid}')

            # Show remaining balance
            balance = web3.eth.get_balance(sender)
            balance_in_ether = web3.from_wei(balance, 'ether')
            print(Fore.CYAN + f"Remaining Balance for {sender}: {balance_in_ether} ETH")

            break
        except Exception as e:
            print(Fore.RED + f"Error on attempt {attempt + 1}: {e}")
            if attempt < retries - 1:
                print(Fore.YELLOW + f"Retrying in 5 seconds... ({attempt + 1}/{retries})")
                time.sleep(5)
            else:
                print(Fore.RED + f"Transaction failed after {retries} attempts.")

# Generate a random recipient address
def generate_random_recipient(web3):
    priv = secrets.token_hex(32)  # Generate a new private key
    private_key = "0x" + priv
    recipient = web3.eth.account.from_key(private_key)
    return recipient

# Check if the RPC URL is valid, retry if not
def check_rpc_url(rpc_url, retries=3):
    for attempt in range(retries):
        try:
            web3 = Web3(Web3.HTTPProvider(rpc_url))
            if web3.is_connected():
                print(Fore.GREEN + "Connected to RPC successfully!")
                chain_id = web3.eth.chain_id  # Try to get the chain ID
                print(Fore.CYAN + f"Chain ID: {chain_id}")
                return web3
            else:
                print(Fore.RED + "Failed to connect to RPC. Please check the URL and try again.")
                if attempt < retries - 1:
                    print(Fore.YELLOW + f"Retrying in 5 seconds... ({attempt + 1}/{retries})")
                    time.sleep(5)
        except Exception as e:
            print(Fore.RED + f"Error connecting to RPC on attempt {attempt + 1}: {e}")
            if attempt < retries - 1:
                print(Fore.YELLOW + f"Retrying in 5 seconds... ({attempt + 1}/{retries})")
                time.sleep(5)
        if attempt == retries - 1:
            print(Fore.RED + f"Failed to connect to RPC after {retries} attempts.")
            return None

# Main execution
print_header()
# Ask the user for the RPC URL and check its validity
web3 = None
while not web3:
    rpc_url = input("Please enter the RPC URL: ")
    web3 = check_rpc_url(rpc_url)

# Ask the user for their private key
private_key = input("Please enter your private key : ")
sender = web3.eth.account.from_key(private_key)

# Ask the user how many transactions to process
loop = int(input("How many transactions do you want to process? : "))

# Ask the user how much to send per transaction
amount = float(input("How much Ether to send per transaction (e.g., 0.001)?: "))

for i in range(loop):
    print(Fore.CYAN + f"\nProcessing Transaction {i + 1}/{loop}")
    
    # Generate a new random recipient address for each transaction
    recipient = generate_random_recipient(web3)
    
    # Transfer native currency using sender's address and private key
    TransferNative(sender.address, private_key, recipient.address, amount, web3)

print(Fore.GREEN + "\nAll transactions completed.")
