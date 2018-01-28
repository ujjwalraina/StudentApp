import Connector
import Student
option = 'y'
o = Student.Student()
table = "student"
print('Welcome to Student Management System')
while option == 'y':
    print("\nEnter 1)Add 2)Display 3)Search 4)Delete 5)update 6)exit")
    option = input()
    if option == "1":
        o.add()
        s ="INSERT INTO "+table+" (sname,grade,math,english,science) "+"VALUES "+"('"+o.sname+"','"+o.grade+"',"+str(o.math)+","+str(o.english)+","+str(o.science)+");"
        if Connector.db.query(s):
            print("\nTransaction Failed")
        else:
            print("\nSuccessfully Added")
            s= "select @@identity"
            Connector.db.query(s)
            result = Connector.db.store_result()
            row = result.fetch_row(1)
            print("\nThe sid of the admitted student is:")
            if row:
                print(row)
        Connector.db.commit()
        option = 'y'

    elif option == "2":
        s="Select * from"+" "+table+";"
        Connector.db.query(s)
        result = Connector.db.store_result()
        row = result.fetch_row(result.row_tell())
        if row:
            print(row)
        else:
            print("Empty Set")
        option = 'y'

    elif option == "3":
        sid = (input('enter sid of the student :\n'))
        s = "Select * from"+" "+table+" where sid = "+str(sid)+ ";"
        Connector.db.query(s)
        result = Connector.db.store_result()
        row = result.fetch_row(1)
        if row:
            print(row)
        else:
            print("Empty Set")
        option = 'y'

    elif option == "4":
        sid = int(input('enter sid of the student :\n'))
        s = "delete from" + " " + table + " where sid = " + str(sid) + ";"
        if Connector.db.query(s):
            print("\nTransaction Failed")
        else:
            print("\nSuccessfully Deleted")
        Connector.db.commit()
        option = 'y'

    elif option == "5":
        sid = int(input('enter sid of the student :\n'))
        print("Press 1 to update math marks or 0 for other options")
        update_option = input()
        if update_option == "1":
            print("Enter updated math marks:")
            o.math = int(input())
            s = "update"+ " " + table + " set math="+ str(o.math) +" where sid = " + str(sid) + ";"
            if Connector.db.query(s):
                print("Transaction Failed\n")
            else:
                print("Successfully Updated\n")

        print("Press 1 to update english marks or 0 for other options")
        update_option = input()
        if update_option == "1":
            print("Enter updated english marks:")
            o.english = int(input())
            s = "update" + " " + table + " set english=" + str(o.english) + " where sid = " + str(sid) + ";"
            if Connector.db.query(s):
                print("Transaction Failed\n")
            else:
                print("Successfully Updated\n")

        print("Press 1 to update science marks or 0 to finish")
        update_option = input()
        if update_option == "1":
            print("Enter updated science marks:")
            o.science = int(input())
            s = "update" + " " + table + " set science=" + str(o.science) + " where sid = " + str(sid) + ";"
            if Connector.db.query(s):
                print("Transaction Failed\n")
            else:
                print("Successfully Updated\n")

        avg = (o.math + o.english + o.science) / 3
        if avg < 30:
            o.grade = 'E'
        elif avg >= 30 and avg < 50:
            o.grade = 'D'
        elif avg >= 50 and avg < 65:
            o.grade = 'C'
        elif avg >= 65 and avg < 85:
            o.grade = 'B'
        else:
            o.grade = 'A'
        s = "update" + " " + table + " set grade = " + "'" + o.grade + "'" + " where sid = " + str(sid) + ";"
        print(s)
        Connector.db.query(s)
        s = "Select grade from" + " " + table + " where sid = " + str(sid) + ";"
        print(s)
        Connector.db.query(s)
        result = Connector.db.store_result()
        row = result.fetch_row(1)
        if row:
            print("The updated grade of the student is: ")
            print(row)
        Connector.db.commit()
        option = 'y'

    elif option == "6":
        Connector.db.close()
        print("Changes Committed")
        flag = 'n'

    else:
        print('you have entered invalid input')
option = 'y'