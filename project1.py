import csv
def write_into_csv(info_list):
    file=open('student_info.txt','a')
    file.write(info_list+"\n")

if __name__=='__main__':

    cond=True
    while(cond):
        student_info=input("enter the student details in the following format(name age contact_no email_id):")
        choice=input("is the entered information correct?")
        if choice=="yes":
            write_into_csv(student_info)
            cond_check=input("enter the yes/no if want to enter another students details: ")
            if(cond_check=='yes'):
                cond=True
            elif(cond_check=='no'):
                cond=False
            else:
                print("wrong input")
        else:
            print("please re-enter the values")
