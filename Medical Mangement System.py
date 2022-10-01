import mysql.connector
##printing Welcome note
print("""

=================================================================================

 Welcome to City Hospitals pvt.ltd.

=================================================================================
 """)



##creating database connectivity
passwd=str(input("Enter the database password:")) 

mysql=mysql.connector.connect(host="localhost",user="root",passwd=passwd,)
mycursor=mysql.cursor()


#creating database 

mycursor.execute("create database if not exists city_hospitals")
mycursor.execute("use city_hospitals")


#creating the tables we need
mycursor.execute("create table if not exists patient_details(puid int(10) primary key,name varchar(30) not null,age int(3),address varchar(50),doctor_recommended varchar(30))")
mycursor.execute("create table if not exists doctor_details(name varchar(30) primary key,specialisation varchar(40),age int(2),address varchar(30),contact varchar(15),fees int(10),monthly_salary int(10))")
mycursor.execute("create table if not exists nurse_details(name varchar(30) primary key,age int(2),address varchar(30),contact varchar(15),monthly_salary int(10))")
mycursor.execute("create table if not exists other_workers_details(name varchar(30) primary key,age int(2),address varchar(30),contact varchar(15),monthly_salary int(10))")


#login or signup option
#creating table for storing the username and password of the user 

mycursor.execute("create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')")


#printing option
print("""
 1. Sign in (Login)
 2. Sign up (Register)
 """)
r=int(input("Enter your choice:"))


#if user wants to register

if r==2:
    print(""" 

=================================================================================
 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Please Register Yourself!!!!!!!!!!!!!!!!!!!!!!!!!!!

=================================================================================
 """)
    u=input("Enter your preferred username!!:")
    p=input("Enter your preferred password (password should be strong!!!:)")


    #entering the entered value to the user_data table
    mycursor.execute("insert into user_data values('"+u+"','"+p+"')")
    mysql.commit()
    print("""

=================================================================================
 !!!!!!!!!!!!!!!!!!!!!!!!!!!Registered Successfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

=================================================================================
 """)
    x=input("Enter any key to continue:")


#if user wants to login
elif r==1:


    #printing the singin option again to the user after registration
    print(""" 

=================================================================================
 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {{sign in }} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

=================================================================================
 """)
    un=input("Enter the username!!: ")
    ps=input("Enter the password!!: ")
    mycursor.execute("Select password from user_data where username='"+un+"'")
    row=mycursor.fetchall()

    for i in row:
        a=list(i)
        if a[0]==str(ps):


            ##displaying the task you can perform
            print("""
 1.Administration
 2.Patient (Admission and Discharge process)
 3.Sign out

 """)


            ##asking for the task from user
            a=int(input("Enter your choice:"))


            #if user wants to enter administration option
            if a==1:
                print("""
 1. Show details
 2. Add new member
 3. Delete existing one
 4. Exit
 """)
                b=int(input("Enter your choice:"))
                #showing the existing details
                if b==1:
                    print("""
 1. Doctor details
 2. Nurse details
 3. Other workers
 """)


                    #asking user's choice
                    c=int(input("Enter your choice:"))


                    #if user wants to see the details of doctors
                    if c==1:
                        mycursor.execute("select*from doctor_details")
                        row=mycursor.fetchall()
                        for i in row:
                            b=0
                            v=list(i)
                            k=["name","specialisation","age","address","contact","fees","monthly_salary"]
                            d=dict(zip(k,v))
                            print(d)


                    #if user wants to see the details of nurses

                    elif c==2:
                        mycursor.execute("select*from nurse_details")
                        row=mycursor.fetchall()
                        for i in row:
                            v=list(i)
                            k=["name","age","address","contact","monthly_salary"]
                            d=dict(zip(k,v))
                            print(d)

                            
                    #if user wants to see the details of other_workers
                    elif c==3:
                        mycursor.execute("select*from other_workers_details")
                        row=mycursor.fetchall()
                        for i in row:
                            v=list(i)
                            k=["name","age","address","contact","monthly_salary"]
                            d=dict(zip(k,v))
                            print(d)

                #if user wants to enter details
                elif b==2:
                    print(""" 
 1. Doctor details
 2. Nurse details
 3. Other workers
 """)
                    c=int(input("Enter your choice:"))
                    #for entering details of doctors
                    if c==1:


                        #asking the details
                        name=input("Enter Dr.name:")
                        spe=input("Enter Specialisation:")
                        age=input("Enter Age:")
                        add=input("Enter Address:")
                        cont=input("Enter Contact no.:")
                        fees=int(input("Enter Fees:"))
                        ms=int(input("Enter monthly_salary:"))


                        #inserting values entered into the doctors_table

                        mycursor.execute("insert into doctor_details values('"+name+"','"+spe+"','"+age+"','"+add+"','"+cont+"','"+str(fees)+"','"+str(ms)+"')")
                        mysql.commit()
                        print("Successfully Added")
                    #for entering nurse details
                    elif c==2:
                        #asking the details
                        name=input("Enter Nurse Name:")
                        age=input("Enter Age:")
                        add=input("Enter Address:")
                        cont=input("Enter Contact no.:")
                        ms=int(input("Enter monthly_salary:"))


                        #inserting values entered to the table
                        mycursor.execute("insert into nurse_details values('"+name+"','"+age+"','"+add+"','"+cont+"','"+str(ms)+"')")
                        mysql.commit()
                        print("Successfully Added")


                    #for entering workers details
                    elif c==3:
                        #asking the details

                        name=input("Enter worker name:")
                        age=input("Enter age:")
                        add=input("Enter address:")
                        cont=input("Enter contact no.:")
                        ms=int(input("Enter monthly_salary:"))


                        #inserting values entered to the table
                        mycursor.execute("insert into other_workers_details values('"+name+"','"+age+"','"+add+"','"+cont+"','"+str(ms)+"')")
                        mysql.commit()
                        print("Successfully Added")
                #if unser wants to delete data
                elif b==3:
                    print("""
 1. Doctor details
 2. Nurse details
 3. Other workers
 """)
                    c=int(input("Enter your choice:"))


                    #deleting doctor's details
                    if c==1:
                        name=input("Enter doctor's name:")
                        mycursor.execute("select*from doctor_details where name=='"+name+"'")
                        row=mycursor.fetchall()
                        print(row)
                        p=input("You really wanna delete this data? (y/n):")
                        if p=="y":
                            mycursor.execute("delete from doctor_details where name='"+name+"'")
                            mysql.commit()
                            print("Successfully Deleted!!")
                        else:
                            print("Not Deleted")


                    #deleting nurse details 

                    elif c==2:
                        name=input("Enter nurse name:")
                        mycursor.execute("select*nurse_details where name=='"+name+"'")
                        row=mycursor.fetchall()
                        print(row)
                        p=input("You really wanna delete this data? (y/n):")
                        if p=="y":
                            mycursor.execute("delete from nurse_details where name='"+name+"'")
                            mysql.commit()
                            print("Successfully Deleted!!")
                        else:
                            print("Not Deleted")


                    #deleting other_workers details
                    elif c==3:
                        name=input("Enter the worker name:")
                        mycursor.execute("select*from workers_details where name=='"+name+"'")
                        row=mycursor.fetchall()
                        print(row)
                        p=input("You really wanna delete this data? (y/n):")
                        if p=="y":
                            mycursor.execute("delete from other_workers_details where name='"+name+"'")
                            mysql.commit()
                            print("Successfully Deleted!!")
                        else:
                            print("Not Deleted")


                elif b==4:
                    break


            #entering the patient details table 

            elif a==2:
                print("""
 1. Show patient details
 2. Add new patient 
 3. Discharge patient
 4. Exit
 """)
                b=int(input("Enter your choice:"))



                #showing the existing details
                #if user wants to see the details of patient
                if b==1:
                    mycursor.execute("select*from patient_details")
                    row=mycursor.fetchall()
                    for i in row:
                        b=0
                        v=list(i)
                        k=["paitent_id","name","age","address","doctor_recommended"]
                        d=dict(zip(k,v))
                        print(d)


                #adding new patient
                elif b==2:
                    paitent_id=input("Enter Paitent_id:")
                    name=input("Enter name: ")
                    age=input("Enter age: ")
                    address=input("Address: ")
                    doctor_recommended=input("Doctor Recommended: ")
                    
                    mycursor.execute ("insert into patient_details values('"+paitent_id+"','"+name+"','"+age+"','"+address+"','"+doctor_recommended+"')")
                    mysql.commit()
                    mycursor.execute("select*from patient_details")
                    print("""

=================================================================================
 !!!!!!!!!!!!!!!!!!!!!!!!!!!Registered Successfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

=================================================================================
""")
                #dischare process
                elif b==3:
                    name=input("Enter Paitent Name: ")
                    mycursor.execute("select*from patient_details where name='"+name+"'")
                    bill=input("has he/she paid all the bills ? (y/n):")
                    if bill=="y":
                        mycursor.execute("delete from patient_details where name='"+name+"'")
                        mysql.commit()
                    else:
                        print("Bill has not been paid")


                #if user wants to exit
                elif b==4:
                    break


            ###sign out
            elif a==3:
                break


            #if the username and password is not in the database
            else:
                break
            
