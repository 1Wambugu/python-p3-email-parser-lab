import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        if not self.email_addresses:
            return []

        email_list = re.split(r'[,\s]+', self.email_addresses)
        unique_emails = list(set(email_list))
        unique_emails.sort()
        return unique_emails
