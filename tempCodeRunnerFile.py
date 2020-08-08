#Figure 1: compare different Cut Operations
    # plt.figure(figsize=(16, 4))
    # plt.title("Figure 1: Different Cut Operations Comparison while using '+' as Paste Method")
    # plt.plot(timeslist, cutList_assignment, 's-', color = 'r', label = "assignment '='") #red
    # plt.plot(timeslist, cutList_copy, 'o-',  color = 'g', label = "copy.copy()") #green
    # plt.plot(timeslist, cutList_deepcopy, '+-' , color = 'b', label = "copy.deepcopy()") #blue
    # plt.plot(timeslist, cutList_pyperclip, 'p-',  color = 'y', label = "Pyperclip") #Yelloe
    # plt.plot(timeslist, cutList_stringformatting, '*-' , color = 'c', label = "string formatting") #c
    # plt.xlabel('Amount of Repeated Cut & Paste Operations')
    # plt.ylabel('Time Spent (second)')    
    # plt.legend(loc = "best")
    # plt.show()

    # #Figure 2: compare different Cut Operations (without pyperclip)
    # plt.figure(figsize=(16, 4))
    # plt.title("Figure 2: Different Cut Operations Comparison while using '+' as Paste Method (Without Pyperclip)")
    # plt.plot(timeslist, cutList_assignment, 's-', color = 'r', label = "assignment '='") #red
    # plt.plot(timeslist, cutList_copy, 'o-',  color = 'g', label = "copy.copy()") #green
    # plt.plot(timeslist, cutList_deepcopy, '+-' , color = 'b', label = "copy.deepcopy()") #blue
    # plt.plot(timeslist, cutList_stringformatting, '*-' , color = 'c', label = "string formatting") #c
    # plt.xlabel('Amount of Repeated Cut & Paste Operations')
    # plt.ylabel('Time Spent (second)')    
    # plt.legend(loc = "best")
    # plt.show()

    # #Figure 3: compare different Cut Operations (without pyperclip or string formatting)
    # plt.figure(figsize=(14, 4))
    # plt.title("Figure 3: Different Cut Operations Comparison while using '+' as Paste Method (Without Pyperclip and String Formatting)")
    # plt.plot(timeslist, cutList_assignment, 's-', color = 'r', label = "assignment '='") #red
    # plt.plot(timeslist, cutList_copy, 'o-',  color = 'g', label = "copy.copy()") #green
    # plt.plot(timeslist, cutList_deepcopy, '+-' , color = 'b', label = "copy.deepcopy()") #blue
    # plt.xlabel('Amount of Repeated Cut & Paste Operations')
    # plt.ylabel('Time Spent (second)')    
    # plt.legend(loc = "best")
    # plt.show()

    # #==========================================================
    # #Figure 4: compare different Paste Operations
    # plt.figure(figsize=(16, 4))
    # plt.title("Figure 4: Different Paste Operations Comparison while using Assignment '=' as Cut Method")
    # plt.plot(timeslist, pasteList_plus, 's-', color = 'r', label = "'+'") #red
    # plt.plot(timeslist, pasteList_percent, 'o-',  color = 'g', label = "%") #green
    # plt.plot(timeslist, pasteList_fstring, '+-' , color = 'b', label = "f-string") #blue
    # plt.plot(timeslist, pasteList_join, 'p-',  color = 'y', label = "str.join()") #Yelloe
    # plt.plot(timeslist, pasteList_format, '*-' , color = 'c', label = "str.format()") #c
    # plt.xlabel('Amount of Repeated Cut & Paste Operations')
    # plt.ylabel('Time Spent (second)')    
    # plt.legend(loc = "best")
    # plt.show()

    # #Figure 5: compare different Paste Operations (without f-string)
    # plt.figure(figsize=(16, 4))
    # plt.title("Figure 5: Different Paste Operations Comparison while using Assignment '=' as Cut Method (without f-string)")
    # plt.plot(timeslist, pasteList_plus, 's-', color = 'r', label = "'+'") #red
    # plt.plot(timeslist, pasteList_percent, 'o-',  color = 'g', label = "%") #green
    # plt.plot(timeslist, pasteList_join, 'p-',  color = 'y', label = "str.join()") #Yelloe
    # plt.plot(timeslist, pasteList_format, '*-' , color = 'c', label = "str.format()") #c
    # plt.xlabel('Amount of Repeated Cut & Paste Operations')
    # plt.ylabel('Time Spent (second)')    
    # plt.legend(loc = "best")
    # plt.show()

    # #=======================
    # #Figure 6: show best cut-paste performance: assignment '=' & str.join()
    # plt.figure(figsize=(16, 4))
    # plt.title("Figure 6: Show Best Cut-Paste Performance (using assignment '=' & str.join())")
    # plt.plot(timeslist, pasteList_join,'s-', color = 'r') #red
    # plt.xlabel('Amount of Repeated Cut & Paste Operations')
    # plt.ylabel('Time Spent (second)')    
    # for a, b in zip(timeslist, pasteList_join):
    #     plt.text(a, b, b, ha='center', va='bottom', fontsize=5)
    # plt.legend(loc = "best")
    # plt.show()

    # #Figure 7: show best copy-paste performance: assignment '=' & str.join()
    # plt.figure(figsize=(16, 4))
    # plt.title("Figure 7: Show Best Copy-Paste Performance (using assignment '=' & str.join())")
    # plt.plot(timeslist, bestCopyList,'s-', color = 'r') #red
    # plt.xlabel('Amount of Repeated Copy & Paste Operations')
    # plt.ylabel('Time Spent (second)')    
    # for a, b in zip(timeslist, bestCopyList):
    #     plt.text(a, b, b, ha='center', va='bottom', fontsize=5)
    # plt.legend(loc = "best")
    # plt.show()