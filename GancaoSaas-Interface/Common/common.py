from Login import login


token = login.login()
headers = {"content-type": "application/json", "access_shop": "199", "access_version": "development", "access_token": token}
