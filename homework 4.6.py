from collections import namedtuple

                          ########## homework ##########
# Masala-1
Car = namedtuple('Car', ('brand', 'model', 'year', 'price'))

car1 = Car(brand='Tesla', model='Model 3', year='2021', price='50000')
car2 = Car(brand='Toyota', model='Corolla', year='2022', price='20000')
car3 = Car(brand='Chevrolet', model='Kobalt', year='2007', price='15000')
car4 = Car(brand='Mersadez', model='S Class', year='2024', price='150000')
car5 = Car(brand='BMW', model='X7', year='2019', price='200000')
car6 = Car(brand='Chevrolet', model='Matiz', year='2006', price='10000')

cars = [car1, car2, car3, car4, car5, car6]

for car in cars:
    if int(car.year) > 2020:
        print(f"Brand: {car.brand}, Model: {car.model}, Year: {car.year}, Price: {car.price}")

# Masala-2
Player = namedtuple('Player', ('name', 'position', 'score'))
players = [
            Player('Madinaxon', 'Hujumchi', 95),
            Player('Nasiba', 'Himoyachi', 90),
            Player('Ali', 'Darvozabon', 100),
            Player('Asad', 'Yarim himoyachi', 45),
            Player('Diyor', "O'ng qanot himoyachisi", 88)
]

natija = max(players, key=lambda player: player.score)
print(f"Eng yuqori natija: {natija.name} ({natija.position}) - {natija.score} ball")

# Masala-3
Book = namedtuple('Book', ('title', 'author', 'year', 'price'))

book1 = Book(title='Otkan kunlar', author='Abdulla Qodiriy', year='1926', price='50000')
book2 = Book(title='Ulugbek xazinasi', author='Abdulla Qahhor', year='2017', price='70000')
book3 = Book(title='Hamsa', author='Alisher Navoiy', year='1483', price='12000 0')
book4 = Book(title='Bir kunlik dunyo', author='bdulla Qahhor', year='1965', price='45000')
book5 = Book(title="Songgi oq", author='Abdulla Qodiriy', year='2019', price='80000')

books = [book1, book2, book3, book4, book5]

natija = sum(int(book.price) for book in books if int(book.year) > 2015)
print(f"Kitob narxi: ${natija}")



# Masala-4
Employee = namedtuple('Employee', ('name', 'position', 'salary', 'experience'))
employees = [
    Employee(name='Ali', position='Developer', salary=1500, experience=8),
    Employee(name='Vali', position='Designer', salary=1200, experience=2),
    Employee(name='Dilshod', position='Manager', salary=2000, experience=5),
    Employee(name='Laylo', position='Analyst', salary=1400, experience=10)
]
tajriba = [i for i in employees if i.experience > 5]
maosh = max(tajriba, key=lambda x: x.salary)
print(f"{maosh.name} - Tajriba: {maosh.experience} yil")

# Masala-5
Competition = namedtuple('Competition', ['team', 'points'])
teams = [
    Competition(team='Team A', points=85),
    Competition(team='Team B', points=78),
    Competition(team='Team C', points=92),
    Competition(team='Team D', points=75)
]

tartiblash = sorted(teams, key=lambda x: x.points, reverse=True)
kuchli_jamoa = tartiblash[0]
print(f"Eng kuchli jamoa: {kuchli_jamoa.team} - {kuchli_jamoa.points} ochko")

# Masala-6
Weather = namedtuple('Weather', ['city', 'temperature', 'humidity'])
cities_weather = [
    Weather(city='Tashkent', temperature=25, humidity=40),
    Weather(city='Samarkand', temperature=22, humidity=50),
    Weather(city='Bukhara', temperature=30, humidity=20),
    Weather(city='Khiva', temperature=28, humidity=30)
]

hot_cities = [city for city in cities_weather if city.temperature > 25]
print("Issiq shaharlar:")
for idx, city in enumerate(hot_cities, start=1):
    print(f"{idx}. {city.city} - {city.temperature}В°C")

# Masala-7
Student = namedtuple('Student', ['name', 'math_score', 'english_score'])

students = [
    Student(name='Ali', math_score=88, english_score=75),
    Student(name='Guli', math_score=95, english_score=80),
    Student(name='Vali', math_score=72, english_score=65),
    Student(name='Laylo', math_score=89, english_score=90)
]

highest_math_student = max(students, key=lambda student: student.math_score)

print(f"Eng yuqori matematika bahosi: {highest_math_student.name} ({highest_math_student.math_score})")