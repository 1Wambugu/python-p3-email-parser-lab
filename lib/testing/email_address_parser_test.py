from lib.email_address_parser import EmailAddressParser

def test_email_address_parser():
    parser = EmailAddressParser("john@doe.com, person@somewhere.org")
    result = parser.parse()
    assert result == ["john@doe.com", "person@somewhere.org"]

    parser = EmailAddressParser("person@somewhere.org john@doe.com")
    result = parser.parse()
    assert result == ["john@doe.com", "person@somewhere.org"]

    parser = EmailAddressParser("john@doe.com, person@somewhere.org, john@doe.com")
    result = parser.parse()  # Corrected this line
    assert result == ["john@doe.com", "person@somewhere.org"]

    parser = EmailAddressParser("person@somewhere.org")
    result = parser.parse()
    assert result == ["person@somewhere.org"]

    parser = EmailAddressParser("")
    result = parser.parse()
    assert result == []
