from sys import maxsize

class Contact:
    def __init__(self, name=None, last_name=None, mobile_phone=None, company=None, id = None,
                 homephone = None, workphone = None, secondaryphone = None, all_phones = None, address = None,
                 all_emails=None, email =None, email2 =None, email3 =None ):
        self.name = name
        self.last_name = last_name
        self.homephone = homephone
        self.mobile_phone = mobile_phone
        self.company = company
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id =id
        self.all_phones_from_home_page = all_phones
        self.address = address
        self.all_emails_from_home_page = all_emails
        self.email = email
        self.email2 = email2
        self.email3 = email3

    def __repr__(self):
        if self.id == None:
            return self.last_name + " " + self.name
        else:
            return self.id+":" + self.last_name +" " + self.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name==other.name and self.last_name==other.last_name


