# An insecure password locker

import sys
import pyperclip

# Note that these are not real passwords
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print(f"Usage: python pw.py [account] -- will copy password to clipboard.")
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
else:
    print(f"There is no account named {account} in the stored passwords")
