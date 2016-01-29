#(1) Using list
 
class PhoneBookList(object):

  '''
    This class uses lists to create a phonebook
  '''

  def __init__(self):
    self.book = []

  def add_contact(self, user_name, phone_number):
    self.book.append([user_name,phone_number])

  '''
    
  '''

  def search(self, username):
    count = 0
    for x, y in self.book:
      count += 1
      if x == username:
        result = {
          'count': count,
          'name': x,
          'phone_number': y
        }
        return result

    return "%s Not found %d" % (username, count)