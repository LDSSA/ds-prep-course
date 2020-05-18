class House:

    def __init__(self, price, area, location):
        self.price = price
        self.area = area
        self.location = location

    def calculate_price_square_meter(self):
        return self.price/self.area

def avg_price(list_houses, location):
    count = 0
    sum_price = 0
    for house in list_houses:
        if house.location == location:
            count+=1
            sum_price+=house.calculate_price_square_meter()
    return sum_price/count

location = "Coimbra"  
