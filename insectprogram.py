import insectclass as c

mosquito = c.Insect(2,4,"Sally")
housefly = c.Insect(2,4,"Bob")

mosquito.flightime()
housefly.flightime()


print(f"the mosquito is named {mosquito.getname()} and can fly up to {mosquito.getflighttime()} miles")
print(f"the housefly is named {housefly.getname()} and can fly up to {housefly.getflighttime()} miles")