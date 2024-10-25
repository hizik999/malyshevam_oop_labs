class Visogod:
    def __init__(self, year):
        self.year = year
    
    def is_leap(self):
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    def __str__(self):
        return f"{self.year + 1} " + (f"True" if self.is_leap() else "False")
    

year = Visogod(2016)
print(year)
year = Visogod(2014)
print(year)