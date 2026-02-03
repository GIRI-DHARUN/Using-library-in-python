from solders.keypair import Keypair
import base58

create_keypair = Keypair()

print("Address:",create_keypair.pubkey())
print("Private Key:",create_keypair.secret())