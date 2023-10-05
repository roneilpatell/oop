import PatientClass as Pa
import ProcedureClass as Pr


patient1 = Pa.Patient(1,'Matt Jones', '123 Main st, Waco TX 76706', '254-555-7415', True)



procedure1= Pr.Procedure('Physical Exam', '2/15/2022', 'Dr.Irvine',250,1)
procedure2= Pr.Procedure('MRI', '2/15/2022', 'Dr.Hamilton',1500,1)
procedure3= Pr.Procedure('CT Scan', '2/17/2022', 'Dr.Drey',1200,2)


patients = [patient1]

procedures = [procedure1,procedure2,procedure3]
total = 0


for patient in patients:
    print("**Patient Bill**")
    print("Name:", patient.get_name())
    print("Address:", patient.get_address())
    print("Phone:", patient.get_phone())
    print()

for procedure in procedures:
    if(patient1.get_id() == procedure.get_patient_id()):
        print("Procedure:", procedure.get_name())
        print("Date:", procedure.get_date())
        print("Practitioner:", procedure.get_practionioner())
        print("Charge: $", procedure.get_charge())
        print()
        print()
        if(patient1.get_veteran_status() == True):
            discount = 0.6
            total += procedure.get_charge() * discount
    
print("Total Charges: $", total)






















