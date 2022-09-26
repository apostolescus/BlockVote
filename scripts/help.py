from brownie import accounts, config


def generate_account(type_of_key):
    if type_of_key == 1:
        account = accounts[0]
        print(account)

    # safe way to store keys
    elif type_of_key == 2:
        account = account.load("myprivatekey")
        print(account)

    # store in env variables
    elif type_of_key == 3:
        account = accounts.add(config["wallets"]["from_key"])

    return account
