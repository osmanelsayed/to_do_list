
to_do_list = []

while(True):
    user = input("please inter the action ( add  , view , remove , exit  )")
    
    if user == "add":
        task = input("inter the task : ")
        to_do_list.append(task)
        print("task added")

    elif user ==  "view":
        if not  to_do_list :
           print("no tasks to view ")
        elif  to_do_list:
            print(to_do_list)
            
    elif user ==  "remove":
        if not  to_do_list :
           print("no tasks to remove ")
        elif  to_do_list:
            taskremove = input("inter task to remove ?")
            to_do_list.remove(taskremove)
            print("task removed")
            
    elif user ==  "exit":
        break
    
    else:
        print("invalid task")
    
    
    
    
    
    


