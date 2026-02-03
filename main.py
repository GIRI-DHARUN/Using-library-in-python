from solders.keypair import Keypair

create_keypair = Keypair()

print("Address:",create_keypair.pubkey())
print("Private Key:",create_keypair.secret())