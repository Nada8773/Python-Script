
#!/usr/bin/python -tt
import sys

# Note                  sys.argv[1] can be (Add ,Remove,ShowAll)


def PhoneBook():

  dict={} # create dictionary
  if str('Add')== sys.argv[1] :    #check for Add
    name = input("Enter the name : ") 
    mail = input("Enter the mail : ")
    phone= input("Enter your phone : ") 
    if mail == '':  #check if there's mail
      mail='NULL'

    dict[name]={mail,phone} # Put your data in dictionary
    
    #add data to database
    file=open('Database.txt','a')
    for i in dict.items():
      file.write(str(i)+'\n')

  
  elif 'Remove' == sys.argv[1]: #check for Remove
    list=[]
    f=open('Database.txt','r')
    name_Remove = input("Enter the name you want to Remove it : ")    
    
    #add data to your database
    for line in f:
      if line[2:2+len(name_Remove)] != name_Remove:  #check if line in the file has name equal to the name you want remove
        list.append(line)
        
    #update your file     
    f.seek(0)    
    f=open('Database.txt','w') 
    print(list)
    for i in list:
      print(i)
      f.write(i)
        
  
  elif 'ShowAll' == sys.argv[1]: #check for Display the data 
    ff=open('Database.txt','r')
    for line in ff.readlines():
      print(line)
  
  else :
    print("Error No Such Order")




if __name__ == '__main__':
  PhoneBook() 