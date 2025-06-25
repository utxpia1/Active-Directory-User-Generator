from pyad import pyad, aduser, adcontainer
import csv

# =======================
# CONFIGURATION SECTION
# =======================

# For this section, the purpose is to automate the OU selection for the new users given that you are already logged in as administrator

# Set connection defaults for pyad
# Use "localhost" if running this script on the Domain Controller
pyad.set_defaults(
        ldap_server="localhost",                # AD server or "localhost" if running
        )

# Define the Organizational Unit (OU) where users will be created in
# Update this to match your AD domain and OU
ou_path = "OU=IT,DC=homelab,DC=local"                   # Defines the destination drawer and where to find it
container = adcontainer.ADContainer.from_dn(ou_path)    # Tells you what drawer handle to use based on the OU defined on the path

# =======================
# PROCESS USERS FROM CSV
# =======================

try:
    # Open the CSV file with user information
    with open("users.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print("CSV Headers:", reader.fieldnames)     # Used to help debug CSV file

        # Loop through each row in the CSV and create the user
        for row in reader:
            full_name = f"{row['FirstName']} {row['LastName']}"  # Combines first and last name
            username = row['Username']
            password = row['Password']

            # Creating the user in Active Directory
            try:
                user = aduser.ADUser.create(
                    username,
                    container,
                    password = password,
                    optional_attributes = {
                        "givenName": row["FirstName"],                          # First name
                        "sn": row["LastName"],                                  # Surname
                        "displayName": full_name,                               # Full name shown in AD
                        "userPrincipalName": f"{username}@homelab.local"        # Login name
                    }
                )
                print(f"[+] Created user: {username}")

            except Exception as user_error:
                print(f"[!] Failed to create user {username}: {user_error}")

except FileNotFoundError:
    print("[!] 'users.csv' not found. Please make sure it's in the same folder.")
except Exception as e:
    print(f"[!] Unexpected error: {e}")
                                           
            
