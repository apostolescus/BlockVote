## add accounts to brownie

brownie accounts new account-name

## accesare cont din script

account = account.load("goeril-owner")

## adaugare conturi in env

.env
export PRIVATE_KEY=0x8f351db3edc74d9b456d912549e90803974499759424cb96adafc2d6d1f1b2d4

brownie-config.yaml

dotenv: .env
wallets:
    from_key: ${PRIVATE_KEY}


from brownie import accounts, config, SmartContract

accounts = accounts.add(config["wallets"]["from_key"])
