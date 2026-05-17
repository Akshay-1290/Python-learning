Ph_no = (input("what is you phone no. :"))
while  len(Ph_no) != 10 or not Ph_no.isdigit():
 print(f"Re-enter a valid phone no.")
 Ph_no=(input("What is your phone number this time fr?? :"))
 if len(Ph_no)==10 :
    print(f"Your phone no. is",Ph_no)
