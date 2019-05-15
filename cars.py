# 8-14

def build_car(make, model, **car_info):
    """Build a dictionary containing everything we know about the car"""
    car = {}
    car['manufacturer'] = make.title()
    car['model'] = model.title()
    for key, value in car_info.items():
        car[key] = value.title()
    return car

car_information = build_car('toyota', '4runner', 
                            color='gray',
                            year='2007')

print(car_information)