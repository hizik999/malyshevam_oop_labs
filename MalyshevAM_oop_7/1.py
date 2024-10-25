class Passport:
    def __init__(self, first_name, last_name, country, date_of_birth, numb_of_passport):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_of_birth = date_of_birth
        self.numb_of_passport = numb_of_passport

    def PrintInfo(self):
        print(f"Passport Info: {self.first_name} {self.last_name}, Country: {self.country}, Date of Birth: {self.date_of_birth}, Passport Number: {self.numb_of_passport}")


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, country, date_of_birth, numb_of_passport, visa):
        super().__init__(first_name, last_name, country, date_of_birth, numb_of_passport)
        self.visa = visa

    def PrintInfo(self):
        super().PrintInfo()
        print(f"Visa Info: {self.visa}")


PassportList = [
    Passport("John", "Doe", "USA", "1990-01-01", "123456789"),
    ForeignPassport("Jane", "Smith", "UK", "1985-05-15", "987654321", "Schengen Visa")
]


for passport in PassportList:
    passport.PrintInfo()
    print()
