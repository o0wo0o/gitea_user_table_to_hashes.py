# gitea_user_table_to_hashes.py

## 🔍 Overview

This script processes a JSON export of the Gitea `user` table and extracts password hashes in the following format: 

username:sha256:50000:base64(salt):base64(hash)

## ⚙️usage:

download json with sqlitebrowser 

```
sqlitebrowser path_to_db
```
![titanic4](https://github.com/user-attachments/assets/fb4be434-fc1e-4b6a-8a7b-a492f049330b)

and then 
```
python3 gitea_user_to_hash.py path_to_file.json
```

Your hashes.txt file will appear.

Next you can do this:

```
hashcat -m 10900 hashes.txt path_to_wordlist --username --force --show
```
