#!/usr/bin/env python3
import subprocess

# clean screen first time
subprocess.run(["clear"])

file_formula = open('docs/formulae_brew.txt', 'r')

for word in file_formula:
    formula_base_rm = word.split() # Save formulae when unnecessary formulas have been deleted
    formula_base = word.split() # save base of formulae

file_formula.close()
choose = [0]

def rstrip_key(key,character): # clean of the end of string(key)
    if character == " ":
        return key.rstrip(" ")
    elif character == ",":
        return key.rstrip(",")

def Remove_Formula_Advance(key,formula_remove):
    global key_error
    key_error = key

    saveIndex = [] # save index need for remove
    saveRemove = [] # save formulae need for remove
    
    if len(key) < 3:
        return "one"
    
    if key[len(key) - 1 ] == " ":
        key = rstrip_key(key," ")
    
    elif key[len(key) - 1] == ",":
        key = rstrip_key(key,",")
    
    # filter numbers form (key)
    for index in range(len(key)):
        if key[index] == ",":
            for i in key.split(","):
                if i.isdigit() == False:
                    return False
                
                saveIndex.append((int)(i))
            break
        
        elif key[index] == " ":
            for i in key.split(" "):
                if i.isdigit() == False:
                    return False
                
                saveIndex.append((int)(i))
            break
        
        elif index == len(key) - 2:
            return False

    # add formulae to saveRemove
    for i in saveIndex:
        if saveIndex.count(i) > 1 or i > len(formula_base) - 1:
            return False
        saveRemove.append(formula_remove[i])

    # Remove formulae
    for i in saveRemove:
        formula_remove.remove(i)
    
    saveIndex.clear()
    saveRemove.clear()

def Remove_Formula(key, formula_remove):
    global key_error
    key_error = key

    # check if it's mixed
    if key.isdigit() == False:
        return False
    
    if (int)(key) > len(formula_remove) - 1:
        return False
    
    saveRemove = []
    saveRemove.append(formula_remove[(int)(key)] )
    formula_remove.remove(saveRemove[0] )

def find_in_FBR(formula): # check if the input(formula) is deleted or not
    for i in formula_base_rm:
        if formula == i:
            return True

def to_task_index_FBR(formula): # get the index of the formula that has been deleted
    for i in formula_base_rm:
        if formula == i:
            return formula_base_rm.index(i)

def menu_display():
    print("Formula({}) Index({})".format(
            
            len(formula_base_rm), 
            len(formula_base_rm) - 1 
        
        ) 
    )
    
    for i in range(0,len(formula_base)):
        if find_in_FBR(formula_base[i]) == True:
            print("   [√]", ": {} ({})".format(
                
                    formula_base[i],
                    to_task_index_FBR(formula_base[i]) 
                ) 
            )

        else:
            print("   [ ]", ": {}".format(formula_base[i] ) )    
    color("6", "| Quit:q | Install:i | Restart:r |", ""); print("\n")
    color("5", "| Remove:d | Delete-data-entry:<Ctrl + u> |", ""); print("\n")

def filter_input():

    #important for deletion mode   
    if choose[0] == "d":
        return "d"
    choose.clear()
    
    # first entry 
    key = input("Your Choose:")
    
    if key == "d":
        choose.append("d")
        return "d"
    
    elif key == "q":
        return "q"

    elif key == "r":
        return "r"
    
    elif key == "i":
        return "i"
    
    else:
        global key_error # Change global variable
        key_error = key
        return False

def color(color, message, more):
    subprocess.run(['sh', 'cmd.sh', 'color' ,color ,message, more])

def restart(message, your_color): # restart or exits
    if your_color == -1:
        
        subprocess.run(["clear"])
        color("1", "[error]" + "-> Remove the formula [index]:", (str)(key_error))
        
        subprocess.run(["echo", ""])
        main()
        return 0

    elif your_color != -1 and your_color != 0:
        color((str)(your_color), message, "")
    key = input()
    
    if key == "y":
        subprocess.run(["./fn.py"])
        return 0
    else:
        return False

def Display():
    while True:
        menu_display()
        
        # filter input from the key
        key = filter_input()
        
        # advance deletion mode
        if key == "d":
            color("5", "--Remove--", "")
            print("\n[index]: 1,2 or 1 2")
            key = input("Remove the formula [index]:")
            status = "mode_focus"

        # options
        match key:
            # key is outside the options
            case False:
                color("1", "Not valid -> [", (str)(key_error) + " ]")
                print("\b ??")
                return restart("Do you want continue[Y/n]",2)
            
            # exit the Programming
            case "q":
                return False
                # break
                    
            # restart
            case "r": 
                return restart("Do you want to start over[Y/n]", 1)

            # install
            case "i":
                return True
        
        # input of the function the Remove_Formula_Advance
        if status == "mode_focus":
            
            # save output of function the Remove_Formula_Advance
            output_RFA = Remove_Formula_Advance(key, formula_base_rm)
            
            if output_RFA == False:
                return restart("", -1)
            
            elif output_RFA == "one":
                if Remove_Formula(key,formula_base_rm) == False:
                    return restart("", -1)
        # clean screen 
        subprocess.run(["clear"])    

def main():        
    output = Display()
    if output == False:
        exit # exit the Programming

    elif output == True:
        
        # convert list -> str
        string = ""
        for i in formula_base_rm:
            string += i
            string += " "
        
        subprocess.run(["printf", ">> brew install "])
        color("2", string, "")
        subprocess.run(["echo", ""])
        print("Do you want continue[Y/n]:", end='')
        
        if input() == "y":
            subprocess.run(['sh', 'cmd.sh', 'brewInstall', string])
        else:
            exit

main()