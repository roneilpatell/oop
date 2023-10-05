class Procedure: 

    def __init__(self,name,date,practionioner,charge,patient_id):
        self.__name = name
        self.__date = date
        self.__practionioner = practionioner
        self.__charge = charge
        self.__patient_id = patient_id

    def get_name(self):
        return(self.__name)
    def get_date(self):
        return(self.__date)
    def get_practionioner(self):
        return(self.__practionioner)
    def get_charge(self):
        return(self.__charge)
    def get_patient_id(self):
        return(self.__patient_id)
    