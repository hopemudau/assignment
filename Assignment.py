def start_program():
    #initialize value to nothing
    value="";
    #create new dictionary
    dictionary={}
    #index to show which entry we are getting
    index=1
    #initialize name to nothing
    name=""
    #initialize age to nothing
    age=""
    #get first input from user
    value=input("Person number "+str(index)+" : ")
    #our stopping is when the user enters -1. Here we check if the input is -1 (stop or continue 
    while value!="-1":
        #Iterate through the whole input from user for us to get the name and age
        for letter in value:
            #check if the current letter is a digit
            if (letter.isdigit()):
                #if the letter is a digit we append it to the age variable
                age+=letter
            else:
                #otherwise append it to the name variable
                name+=letter
        #put the name as the key of the dictionary and age as the value
        dictionary[name]=int(age)
        #increase index for use to prompt the next person
        index+=1
        #get the next person
        value=input("Person number "+str(index)+" : ")
        #reinitialize the name variable to nothing
        name=""
        #reinitialize age to nothing
        age=""
    #sort the dictionary by age getting a list in return and reverse it so that you can get it from top to bottom
    sorted_x = reversed(sorted(dictionary.items(), key=lambda x: x[1]))
    po=1;
    print()
    #iterate through the list from top to bottom
    for key in sorted_x:
        #get the age of someone
        comp_age=dictionary[key[0]]
        #check is the rule of entry applies
        if(comp_age>17 and comp_age<90):
            #if it does, print that this person is allowed to enter at a certain position allowing older people to enter first
            print (key[0]+" is allowed to enter and as entry number "+str(po))
            po+=1
        else:
            #otherwise they are not allowed to enter
            print (key[0]+" is not allowed to enter")
    return sorted_x
if __name__ == '__main__':
    list_sorted= start_program()
    print(list)
