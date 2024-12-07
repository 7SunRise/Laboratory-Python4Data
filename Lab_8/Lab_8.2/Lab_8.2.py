from sqlalchemy import ForeignKey, create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///deliveryOrder.db", echo=True) # обьект engine отвечает за все соединения
Base = declarative_base() # базовый класс

class Courier(Base): # таблица курьеров
	__tablename__ = "courier"

	id = Column(Integer, primary_key=True)
	surname = Column(String)
	name = Column(String)
	secondName = Column(String)
	passportNumber = Column(String)
	dateOfBirth = Column(String)
	dateOfEmployment = Column(String)
	clockInTime = Column(String)
	clockOutTime = Column(String)
	city = Column(String)
	street = Column(String)
	houseNumber = Column(String)
	apartmentNumber = Column(String)
	phoneNumber = Column(String)

class Transport(Base): # таблица транспортов
	__tablename__ = "transport"

	number = Column(Integer, primary_key=True)
	carBrand = Column(String)
	dateOfRegistration = Column(String)
	colour = Column(String)

class Sender(Base): # таблица отправителей
    __tablename__ = 'sender'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    secondName = Column(String)
    dateOfBirth = Column(String)
    index = Column(String)
    city = Column(String)
    street = Column(String)
    houseNumber = Column(String)
    apartmentNumber = Column(String)
    phoneNumber = Column(String)

class Receiver(Base): # таблица получателей
    __tablename__ = 'receiver'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    secondName = Column(String)
    dateOfBirth = Column(String)
    index = Column(String)
    city = Column(String)
    street = Column(String)
    houseNumber = Column(String)
    apartmentNumber = Column(String)
    phoneNumber = Column(String)

class Order(Base): # таблица заказов
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    idSender = Column(Integer, ForeignKey('sender.id'))
    sender = relationship('Sender')
    idReceiver = Column(Integer, ForeignKey('receiver.id'))
    receiver = relationship('Receiver')
    dateOfOrder = Column(String)
    dateOfDelivery = Column(String)
    priceOfDelivery = Column(Integer)
    idCourier = Column(Integer, ForeignKey('courier.id'))
    courier = relationship('Courier')
    transportNumber = Column(Integer, ForeignKey('transport.number'))
    transport = relationship('Transport')

Base.metadata.create_all(engine) # Метаданные нашей БД
Session = sessionmaker(bind=engine) # создаем сессию для того, чтобы добавлять данные в базу
session = Session()

# Добавляем данные в таблицу отправителей
sender1 = Sender(id=1, surname='DiCaprio', name='Leonardo', secondName='Wilhelm', dateOfBirth='11.1.1974', index="000001", city='City1', street='Street1', houseNumber="1", apartmentNumber="1", phoneNumber='+00000000001')
session.add(sender1)
sender2 = Sender(id=2, surname='Depp', name='John', secondName='Chistopher', dateOfBirth='09.06.1963', index="000002", city='City2', street='Street2', houseNumber="2", apartmentNumber="2", phoneNumber='+00000000002')
session.add(sender2)
session.commit()

# Добавляем данные в таблицу получателей
receiver1 = Receiver(id=1, surname='Pitt', name='William', secondName='Bradley', dateOfBirth='18.12.1963', index="000003", city='City3', street='Street3', houseNumber="3", apartmentNumber="3", phoneNumber='+00000000003')
session.add(receiver1)
receiver2 = Receiver(id=2, surname='Downey Jr.', name='Robert', secondName='John', dateOfBirth='04.04.1965', index="000004", city='City4', street='Street4', houseNumber="4", apartmentNumber="4", phoneNumber='+00000000004')
session.add(receiver2)
session.commit()

# Добавляем данные в таблицу заказов
order1 = Order(id=1, idSender=1, idReceiver=2, dateOfOrder='01.01.2001', dateOfDelivery='01.01.2001', priceOfDelivery=100, idCourier=1, transportNumber="A000AA")
session.add(order1)
order2 = Order(id=2, idSender=1, idReceiver=1, dateOfOrder='02.02.2002', dateOfDelivery='02.02.2002', priceOfDelivery=200, idCourier=1, transportNumber="A000AA")
session.add(order2)
session.commit()