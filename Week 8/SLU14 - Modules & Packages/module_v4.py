import numpy as np

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

if __name__ == "__main__":
    
    array_houses_coimbra = np.array([[150000, 200],
                                     [120000, 150], 
                                     [100000, 100],
                                     [250000, 250],
                                     [175000, 200]])   
    
    list_houses = []

    for i in array_houses_coimbra:
        price = i[0]
        area = i[1]
        list_houses.append(House(price, area, location))
    
    avg_price_coimbra = avg_price(list_houses, location)

    print("Average price of houses in Coimbra per square meter is {}".format(avg_price_coimbra))
