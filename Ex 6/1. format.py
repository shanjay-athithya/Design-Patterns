class Stock:
    def __init__(self, company, rate, date, time):
        self.company = company
        self.rate = rate
        self.date = date
        self.time = time

    def display(self):
        print(f"{self.company:<10} {self.rate:<10} {self.date:<12} {self.time:<10}")

if __name__ == "__main__":
    stocks = []
    with open("D:\PYTHON Code\SEM 3\Ex 6\stock.txt", "r") as s:
        for line in s:
            words = line.strip().split()
            if len(words) == 4:
                company, rate, date, time = words
                stocks.append(Stock(company, rate, date, time))
    for stock in stocks:
        stock.display()
