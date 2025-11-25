from email_address_parser import EmailAddressParser

class TestEmailAddressParser:
    '''Class EmailAddressParser in email_address_parser.py'''

    def test_instantiates_with_string(self):
        '''instantiates with a single argument, a string.'''
        
    def test_has_parse_method(self):
        '''contains a method called "parse".'''
        
    def test_parses_emails_with_spaces(self):
        '''finds emails with spaces in between.'''
        parser = EmailAddressParser("talk@talk.com john.jones@flatironschool.com alexa@amazon.com")
        
    def test_parses_emails_with_commas(self):
        '''finds emails with commas in between.'''
       
    def test_parses_emails_with_commas_and_spaces(self):
        '''finds emails with commas and spaces in between.'''
        
    def test_parses_emails_with_commas_and_spaces_and_non_emails(self):
        '''finds emails with commas and spaces in between and removes non-email strings.'''
        