# Hospital Management System (Lite Edition)

# Step 1: Create lists for patients and bills
patients = []
bills = []
# Step 2: Create a dictionary for health issues mapping to respective doctors
doctors = {"fever": "Dr Hussain (General Physician)",
           "cold": "Dr Gregory House (General Physician)",
           "heart" : "Dr Who (Cardiologist)",
           "bones" : "Dr Zeuss (Orthopedic)",
           "skin" : "Dr Frankenstein (Dermatologist)",
           "eye" : "Dr Mike Wazaowski (Opthalmologist)"}

# Step 3: Create a dictionary for services and respective cost
services = {"Checkup" : 100,
           "X-Ray": 200,
           "Lab Test" : 300,
           "Injection": 50,
           "EGC": 1000}

# Print welcome message
print("Welcome to Atomcamp Hospital Management System! \n")

# Step 5: Create main loop for program
while True:
  print("Select an option")
  print("Enter 1 for Registering a New Patient")
  print("Enter 2 for Viewing All Patients")
  print("Enter 3 for Searching Patient by Doctor or Symptom")
  print("Enter 4 for Generating a Billfor The Patient")
  print("Enter 5 for Showing Unique Symptoms")
  print("Enter 6 to Exit the Hospital")

  choice = input("Enter your choice(1-6): ")
  if choice == "1":
    name = input("Enter the patient's name: ")
    age = int(input("Enter the patient's age: "))
    occupation = input("Enter the occupation of the patient: ")
    symptom = input("Enter the main symptom of the patient: ")

    assigned_doctor = doctors.get(symptom, "Dr. Hussain (General Physician)")
    
    patient = (name, age, occupation, symptom, assigned_doctor)
    patients.append(patient)
    print(f"Patient {name} has been registered and assigned to {assigned_doctor}.")

  elif choice == "2":
    if not patients:
      print("No patients are registered yet.")
    else:
      print("Here is the list of the registered patients: ")
      for patient in patients:
        print(f"Name of the patient: {patient[0]} | Age of the patient: {patient[1]} | Occupation of the pateint: {patient[2]} | Symptom of the patient: {patient[3]} | The doctor assigned to the patient: {patient[4]}")
        print()

  elif choice == "3":
    
    search_key = input("Enter the name of the doctor or the symptom: ")
    found = False
    print("\n Search Results: ")

    for patient in patients:
      if search_key in patient[4] or search_key in patient[3]:
        print(f"Name of the patient: {patient[0]} | Age of the patient: {patient[1]} | Occupation of the pateint: {patient[2]} | Symptom of the patient: {patient[3]} | The doctor assigned to the patient: {patient[4]}")
        found = True
        
      if not found:
        print("No matching patients found \n")
      print()
      
  elif choice == "4":
    name = input("Enter the name of the patient: ")
    found = False
    
    for patient in patients:
      if patients[0] == name:
        found = True
        print("\n Available Services: ")

        for service, charges in services.items():
          print(f"{service}: {charges}")

        selected = []
        total = 0

        while True:
          service_the_patient_wants = input("Enter the service name to add (type done to finish): ")
          if service_the_patient_wants == "done":
            break
          elif service_the_patient_wants in services:
            selected.append(service_the_patient_wants)
            total += services[service_the_patient_wants]
            
          else:
            print("Invalid Input!")

        bill = (name, selected, total)
        bills.append(bill)

        print(f"Bill for {name}")
        print("Services: ", selected)
        print("Total: ", total)
        print()
    if not found:
      print("Patient not found \n")

  elif choice == "5":
    symptoms_set = set()
    for patient in patients:
      symptoms_set.add(patient[3])
    print("Unique Symptoms Registered: ")

    for symptom in symptoms_set:
      print(symptom)
    print()

  elif choice == "6":
    print("\n Thankyou for Visiting the Hospital! \n")
    break
    
  else:
    print("Invalid Input!")