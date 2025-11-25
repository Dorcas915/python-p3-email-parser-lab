class EmailAddressParser:
    def __init__(self, emails_string):
        self.emails_string = emails_string

    def parse(self):
        if not self.emails_string:
            return []
        
        return [email.strip() for email in self.emails_string.split(",")]
