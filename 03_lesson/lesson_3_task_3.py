from address import Address
from mailing import Mailing


address1 = Address('123456', 'Москва', 'Ленина', '10', '5')
address2 = Address('654321', 'Санкт-Петербург', 'Пушкина', '20', '10')
mailing = Mailing('TRACK123', address1, address2, 1000)
print(mailing)
