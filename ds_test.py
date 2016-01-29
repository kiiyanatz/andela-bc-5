from data_sturcture import PhoneBookList as pb

book = pb()
book.add_contact('kiiyanatz', '0722402490')
book.add_contact('James', '0743455434')
book.add_contact('Erick', '0740000034')
book.add_contact('James', '0721222222')
book.add_contact('Jack', '0733333333')


result = book.search("Jack")
for keys, value in result.items():
  print keys, value