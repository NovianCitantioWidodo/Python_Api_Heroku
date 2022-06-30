import bcrypt

pw = "123ff"
password = pw.encode("utf-8")
print(password)

pw = "$2b$12$ENvs1EpneLAY9K.PQF2Xc.au92RsDkxUL3WF6s8U2X.AEuqsVdH8S"
hashed = pw.encode("utf-8")
print(hashed)

print(bcrypt.checkpw(password, hashed))