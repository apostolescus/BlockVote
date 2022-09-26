from brownie import accounts, config, network, Voting
from phe import paillier, EncryptedNumber
from .helpful_enc import encrypt, add_numbers, decrypt, generate_keys, get_nsquare


def test():

    account = accounts[0]
    account2 = accounts[1]
    account3 = accounts[2]
    account4 = accounts[3]

    (pubkey, privkey) = generate_keys()
    nsquare = get_nsquare()

    # deploy contract
    voting = Voting.deploy({"from": account})

    voting.resetVote(nsquare)
    # add candidates
    voting.addCandidate("Marin", {"from": account})
    voting.addCandidate("Ion", {"from": account})
    voting.addCandidate("Bush", {"from": account})

    # start vote
    print("Starting vote ... ")
    voting.startVote()
    print("Vote Started ...")
    print("----------")

    print("Encrypting first vote ...")
    enc11 = encrypt(pubkey, 0)
    enc21 = encrypt(pubkey, 1)
    enc31 = encrypt(pubkey, 0)
    print("First vote encrypted.")
    print("Encryption result: ", enc11, enc21, enc31)
    print("----------")
    # print(len(str(enc11)))

    print("Sending first vote to blockchain ...")
    voting.vote((enc11, enc21, enc31), {"from": account})
    print("Vote send!")
    print("----------")

    print("Encrypting second vote ... ")
    enc12 = encrypt(pubkey, 0)
    enc22 = encrypt(pubkey, 1)
    enc32 = encrypt(pubkey, 0)
    print("Second vote encrypted!")
    print("Encryption result: ", enc12, enc22, enc32)
    print("----------")

    print("Sending second vote to blockchain ...")
    voting.vote((enc12, enc22, enc32), {"from": accounts[1]})
    print("Vote send!")
    print("----------")

    print("Ending voting session ... ")
    voting.endVote()
    print("Voting session end!")
    print("----------")

    print("Obtaining results ...")
    candidate_results = voting.getFinalResults()
    print("Results fetched!")
    print("----------")

    print(" Encrypted result: ", candidate_results)
    print("----------")

    print("Decrypted results: ")
    for i in candidate_results:
        decrypted_result = decrypt(int(i))
        print(decrypted_result)

    print("Restarting voting session")
    voting.resetVote(nsquare)

    # add candidates
    voting.addCandidate("Marin", {"from": account})
    voting.addCandidate("Ion", {"from": account})
    voting.addCandidate("Bush", {"from": account})

    # start vote
    print("Starting vote ... ")
    voting.startVote()
    print("Vote Started ...")
    print("----------")

    print("Encrypting first vote ...")
    enc11 = encrypt(pubkey, 1)
    enc21 = encrypt(pubkey, 0)
    enc31 = encrypt(pubkey, 0)
    print("First vote encrypted.")
    print("Encryption result: ", enc11, enc21, enc31)
    print("----------")
    # print(len(str(enc11)))

    print("Sending first vote to blockchain ...")
    voting.vote((enc11, enc21, enc31), {"from": account})
    print("Vote send!")
    print("----------")

    print("Encrypting second vote ... ")
    enc12 = encrypt(pubkey, 0)
    enc22 = encrypt(pubkey, 0)
    enc32 = encrypt(pubkey, 1)
    print("Second vote encrypted!")
    print("Encryption result: ", enc12, enc22, enc32)
    print("----------")

    print("Sending second vote to blockchain ...")
    voting.vote((enc12, enc22, enc32), {"from": accounts[1]})
    print("Vote send!")
    print("----------")

    print("Ending voting session ... ")
    voting.endVote()
    print("Voting session end!")
    print("----------")

    print("Obtaining results ...")
    candidate_results = voting.getFinalResults()
    print("Results fetched!")
    print("----------")

    print(" Encrypted result: ", candidate_results)
    print("----------")

    print("Decrypted results: ")
    for i in candidate_results:
        decrypted_result = decrypt(int(i))
        print(decrypted_result)


def deploy():
    account = accounts[0]

    (pubkey, privkey) = generate_keys()
    nsquare = get_nsquare()
    voting = Voting.deploy(nsquare, {"from": account})

    voting.addCandidate("Marin", {"from": account})
    voting.addCandidate("Ion", {"from": account})
    voting.addCandidate("Bush", {"from": account})

    print("Starting vote ... ")
    voting.startVote()
    print("Vote Started ...")
    print("----------")
    candidates = voting.viewCandidates()

    print("Candidates: ", candidates)
    print("----------")

    print("Encrypting first vote ...")
    enc11 = encrypt(pubkey, 0)
    enc21 = encrypt(pubkey, 1)
    enc31 = encrypt(pubkey, 0)
    print("First vote encrypted.")
    print("Encryption result: ", enc11, enc21, enc31)
    print("----------")
    # print(len(str(enc11)))

    print("Sending first vote to blockchain ...")
    voting.vote((enc11, enc21, enc31), {"from": account})
    print("Vote send!")
    print("----------")

    print("Encrypting second vote ... ")
    enc12 = encrypt(pubkey, 0)
    enc22 = encrypt(pubkey, 1)
    enc32 = encrypt(pubkey, 0)
    print("Second vote encrypted!")
    print("Encryption result: ", enc12, enc22, enc32)
    print("----------")

    print("Sending second vote to blockchain ...")
    voting.vote((enc12, enc22, enc32), {"from": accounts[1]})
    print("Vote send!")
    print("----------")

    print("Ending voting session ... ")
    voting.endVote()
    print("Voting session end!")
    print("----------")

    print("Obtaining results ...")
    candidate_results = voting.getFinalResults()
    print("Results fetched!")
    print("----------")

    print(" Encrypted result: ", candidate_results)
    print("----------")

    print("Decrypted results: ")
    for i in candidate_results:
        decrypted_result = decrypt(int(i))
        print(decrypted_result)

    # votes = voting.getVotes(0)

    # print(votes)
    # print(votes)


def main():
    test()

    # deploy()
