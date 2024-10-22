# Auto Send Native Token Bot

## Description
This bot is designed to automatically send native tokens on EVM-compatible chains. The bot is created to support Ethereum Virtual Machine (EVM) chains and allows users to specify the number of transactions, amount to send, and uses a random recipient address each time.

## Features
- Supports any EVM chain
- Allows multiple transactions in one run
- Simple, secure, and easy to use

**Bot created by**: [https://t.me/airdropwithmeh](https://t.me/airdropwithmeh)

## How to Use

### 1. Clone the Repository
To get started, clone the repository to your local machine using Git:

```bash
git clone https://github.com/ganjsmoke/auto-send-native.git
```

```bash
cd auto-send-native-token-bot
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Bot
```bash
python3 bot.py
```

### 4. Input Details
After running the script, you will be prompted to provide:

* RPC URL: The URL of the EVM chain's RPC endpoint.
* Private Key: Your private key for the wallet that will be sending the transactions.
* Number of Transactions: The number of transactions you want to perform.
* Amount of Ether: The amount of Ether to send per transaction.
* Each transaction will be sent to a newly generated random recipient address.
