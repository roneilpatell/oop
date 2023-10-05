import CellPhoneClass as Phone 


def main():

    my_phone1 = Phone.CellPhone('Apple','iPhone','900')
    my_phone2 = Phone.CellPhone('Samsung','Flip', '1000')

    print(f"The phone manufactuer is {my_phone1.get_manufact()} and the model type is {my_phone1.get_model()} and is priced at {my_phone1.get_retail_price()}")
    print(f"The phone manufactuer is {my_phone2.get_manufact()} and the model type is {my_phone2.get_model()} and is priced at {my_phone2.get_retail_price()}")

          

main()

