
Active Directory User Generator

- Automates the creation of Active Directory (AD) user accounts using Python and a CSV file. This project simulates a real-world sysadmin task of onboarding multiple users into a Windows Server domain environment.

---

Features:

- Reads user data (first name, last name, username, password) from a `.csv` file
- Automatically creates user accounts in a specified Organizational Unit (OU)
- Handles display names, user logon names, and secure password assignment
- Supports error handling and can be extended with logging or group assignment
- Tested in a Windows Server VM with Active Directory and Python environment

---

Requirements:

- Python 3.10+
- pyad
- pywin32
- Windows Server VM with Active Directory Domain Services installed

---

How to Use:

1. Set up a Windows Server VM with Active Directory installed (I used VMware to imitate workplace environment).
2. Log in as a domain administrator
3. Create an Organizational Unit (e.g., `IT`)
4. Modify the 'ou_path' in 'create_ad_users.py' to match your OU:
   
	Example:
		ou_path = "OU=IT,DC=yourdomain,DC=local"
   
5. Fill out 'users.csv' using the structure: FirstName,LastName,Username,Password
	Example
		John,Doe,jdoe,Password123!
   
6. Run the script in IDLE or another Python environment

---

What I Learned: 

- Setting up and configuring Window Server virtual machine with VMware.
- Installing, navigating, and configuring Active Directory Domain Services.
- Writing and executing Python scripts to automate administrative tasks.
- Performing real-world IT tasks such as user provisioning, OU management, and password setup.
- Simulating enterprise IT environments in a self-contained lab for hands-on learning.
