command = input("Press Y to enter the contact and N to display the contact :-  ")
if command == "Y":
    fname = input("Enter the First Name :-\n")
    lname = input("Enter the Last Name :-\n")
    phone_no = int(input("Enter the phone number :-\n"))
    alt_contact = int(input("Enter the alternate contact:-\n"))
    email = input("Enter the email address:-\n")
    # Saving the contact information into file
    fa = open(r".\Project_Phone_Directory\contact.txt","at")
    fa.write(f"Name : - {fname+" "+lname} \nPhone No :- {phone_no} \nAlternative No :- {alt_contact} \nEmail : - {email} \n")
    fa.close()
    print("Contact Information Saved Successfully!!")
elif command == "N":
    fp = open(r".\Project_Phone_Directory\contact.txt","rt")
    print(fp.readline())
    fp.close()
else:
    print("Please choose a valid option")