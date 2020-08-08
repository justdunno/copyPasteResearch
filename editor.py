import pyperclip as pc 
import copy
import matplotlib.pyplot as plt

# x-axis
timeslist = list() 

# y-axis
cutList_assignment = list() #use = for cut
cutList_copy = list() #use copy.copy()
cutList_deepcopy = list() #use copy.deepcopy()
cutList_pyperclip = list() #use pyperclip
cutList_stringformatting = list() #use string formatting

pasteList_plus = list() #using '+' for paste
pasteList_percent = list() #use '%' for paste
pasteList_fstring = list() #use f-string
pasteList_join = list() #str.join()
pasteList_format = list() #str.format()

bestCutList = list() #use = for cut & str.join() for paste
bestCopyList = list() #use = for copy & str.join() for paste

class SimpleEditor:
    def __init__(self, document):
        self.document = document
        self.dictionary = set()
        with open("/wft/filesfrom/dictionary.txt") as input_dictionary: # open dictionary file
            for line in input_dictionary:
                words = line.strip().split(" ")
                for word in words:
                    self.dictionary.add(word)
        self.paste_text = ""

    def cut(self, i, j): #original cut method [m0]
        self.paste_text = self.document[i:j]  # '=' assignment
        self.document = self.document[:i] + self.document[j:]

    def copy(self, i, j): #original copy method [m0]
        self.paste_text = self.document[i:j]

    def paste(self, i): #original paste method [m0]
        self.document = self.document[:i] + self.paste_text + self.document[i:]
        #print("paste_text: " + self.paste_text)

    #=========================compare different cut methods====================

    def cut_paste_using_shallowcopy(self, i, j, k): #[m1]: copy.copy() & '+'
        self.paste_text = copy.copy(self.document[i:j])
        self.document =  self.document[:i] + self.document[j:] #remove the cut part in the string
        self.document = self.document[:k] + self.paste_text + self.document[k:] #paste text from clipboard  to k position

    def cut_paste_using_deepcopy(self, i, j, k): #[m2]: copy.deepcopy() & '+'
        self.paste_text = copy.deepcopy(self.document[i:j])
        self.document =  self.document[:i] + self.document[j:]
        self.document = self.document[:k] + self.paste_text + self.document[k:]

    def cut_paste_using_pyperclip(self, i, j, k): #[m3]: pyperclip & '+'
        pc.copy(self.document[i:j]) 
        self.document = self.document[:i] + self.document[j:] 
        self.document = self.document[:k] + pc.paste() + self.document[k:] 

    def cut_paste_using_string_formatting(self, i, j, k): #[m4]: string formatting & '+'
        self.paste_text = '%s' % self.document[i:j]
        self.document = self.document[:i] + self.document[j:] 
        self.document = self.document[:k] + pc.paste() + self.document[k:] 

    #======================================diffrent paste methods: ========================  
    def cut_paste_using_assignment_percent(self, i, j, k): #[m5]
        self.paste_text = self.document[i:j]
        self.document = "%s%s" % (self.document[:i], self.document[j:])
        self.document = "%s%s%s" % (self.document[:k], self.paste_text, self.document[k:]) #use % for concatenation
  
    def cut_paste_using_assignment_fstring(self, i, j, k): #[m6]
        self.paste_text = self.document[i:j]
        self.document = f'{self.document[:i]}{self.document[j:]}' #remove the cut part in the string using f-string
        self.document = f'{self.document[:k]}{pc.paste()}{self.document[k:]}' #use f-string 
    
    def cut_paste_using_assignment_join(self, i, j, k): #[m7]
        self.paste_text = self.document[i:j]
        self.document = "".join([self.document[:i], self.document[j:]]) #remove the cut part in the string using join()
        self.document = "".join([self.document[:k], self.paste_text, self.document[j:]]) #use join() for concatenation
    
    def cut_paste_using_assignment_format(self, i, j, k): #[m8]
        self.paste_text = self.document[i:j]
        self.document = "{}{}".format(self.document[:i], self.document[j:]) #use format() to cut
        self.document = "{}{}{}".format(self.document[:k], self.paste_text, self.document[k:]) #use format() for concatenation


    #=======================
    def copy_paste_using_assignment_join(self, i, j, k): #best copy methods combination: assignment & join()
        self.paste_text = self.document[i:j]
        self.document = "".join([self.document[:k], self.paste_text, self.document[j:]]) #use join() for concatenation
    #=====================

    def get_text(self):
        #return copy.copy(self.document)
        return self.document

    def misspellings(self):
        result = 0
        for word in self.document.split(" "):
            if word not in self.dictionary:
                result = result + 1
        #print("#misspelling: " + str(result))
        return result

import timeit

class EditorBenchmarker:
    new_editor_case = """
from __main__ import SimpleEditor
s = SimpleEditor("{}") """

    #===== method 0 (original): use assignment & '+' ===========
    editor_cut_paste = """
for n in range({}):
    if n%2 == 0: 
        s.cut(1, 3)
    else:
        s.paste(2)"""

    #===== method 1 : use copy.copy() & '+' ===========
    editor_cut_paste_m1 = """
for n in range({}):
    if n%2 == 0: 
        s.cut_paste_using_shallowcopy(1, 3, 2)"""
    #=====

    #===== method 2 : use copy.deepcopy() & '+' ===========
    editor_cut_paste_m2 = """
for n in range({}):
    if n%2 == 0: 
        s.cut_paste_using_deepcopy(1, 3, 2)"""
    #=====

    #===== method 3 : use pyperclip & '+' ===========
    editor_cut_paste_m3 = """
for n in range({}):
    if n%2 == 0: 
        s.cut_paste_using_pyperclip(1, 3, 2)"""
    #=====

    #===== method 4 : use string formatting & '+' ===========
    editor_cut_paste_m4 = """
for n in range({}):
    if n%2 == 0: 
        s.cut_paste_using_string_formatting(1, 3, 2)"""
    #=====

    #===== method 5 : Use assignment '=' and '%' ===========
    editor_cut_paste_m5 = """
for n in range({}):
    if n%2 == 0: 
        s.cut_paste_using_assignment_percent(1, 3, 2)"""
    #=====

     #===== method 6 : assignment '=' and f-string ===========
    editor_cut_paste_m6 = """
for n in range({}):
    if n%2 == 0: 
        s.cut_paste_using_assignment_fstring(1, 3, 2)"""
    #=====

    #===== method 7 : assignment '=' and str.join() ===========
    editor_cut_paste_m7 = """
for n in range({}):
    if n%2 == 0: 
        s.cut_paste_using_assignment_join(1, 3, 2)"""
    #=====

    #===== method 8 : assignment '=' and str.format() ===========
    editor_cut_paste_m8 = """
for n in range({}):
    if n%2 == 0: 
        s.cut_paste_using_assignment_format(1, 3, 2)"""
    #=====

    editor_copy_paste = """
for n in range({}):
    if n%2 == 0:
        s.copy(1, 3)
    else:
        s.paste(2)"""

    editor_copy_paste_best = """
for n in range({}):
    if n%2 == 0:
        s.copy_paste_using_assignment_join(1, 3, 2)"""

    
    editor_get_text = """
for n in range({}):
    s.get_text()"""

    editor_misspellings = """
for n in range({}):
    s.misspellings()"""

    def __init__(self, cases, N):
        self.cases = cases
        self.N = N
        self.editor_cut_paste = self.editor_cut_paste.format(N)
        self.editor_cut_paste_m1 = self.editor_cut_paste_m1.format(N)
        self.editor_cut_paste_m2 = self.editor_cut_paste_m2.format(N)
        self.editor_cut_paste_m3 = self.editor_cut_paste_m3.format(N) #takes the most time
        self.editor_cut_paste_m4 = self.editor_cut_paste_m4.format(N)
        self.editor_cut_paste_m5 = self.editor_cut_paste_m5.format(N)
        self.editor_cut_paste_m6 = self.editor_cut_paste_m6.format(N)
        self.editor_cut_paste_m7 = self.editor_cut_paste_m7.format(N)
        self.editor_cut_paste_m8 = self.editor_cut_paste_m8.format(N)
        self.editor_copy_paste = self.editor_copy_paste.format(N)
        self.editor_copy_paste_best = self.editor_copy_paste_best.format(N)
        self.editor_get_text = self.editor_get_text.format(N)
        self.editor_misspellings = self.editor_misspellings.format(N)

    def benchmark(self):
        for case in self.cases:
            print("Evaluating case: {}".format(case))
            new_editor = self.new_editor_case.format(case)

            cut_paste_time = timeit.timeit(stmt=self.editor_cut_paste, setup=new_editor, number=1) #assignment '=' & '+' 
            print("{} times [m0] cut paste operations took {} s".format(self.N, cut_paste_time))
            cutList_assignment.append(cut_paste_time)
            pasteList_plus.append(cut_paste_time)

            cut_paste_time_m1 = timeit.timeit(stmt=self.editor_cut_paste_m1, setup=new_editor, number=1) # copy.copy() & '+'
            print("{} times [m1] cut paste operations took {} s".format(self.N, cut_paste_time_m1)) 
            cutList_copy.append(cut_paste_time_m1)

            cut_paste_time_m2 = timeit.timeit(stmt=self.editor_cut_paste_m2, setup=new_editor, number=1) #copy.deepcopy() & '+'
            print("{} times [m2] cut paste operations took {} s".format(self.N, cut_paste_time_m2))
            cutList_deepcopy.append(cut_paste_time_m2)            

            cut_paste_time_m3 = timeit.timeit(stmt=self.editor_cut_paste_m3, setup=new_editor, number=1) #pyperclip & '+'
            print("{} times [m3] cut paste operations took {} s".format(self.N, cut_paste_time_m3))
            cutList_pyperclip.append(cut_paste_time_m3)

            cut_paste_time_m4 = timeit.timeit(stmt=self.editor_cut_paste_m4, setup=new_editor, number=1)
            print("{} times [m4] cut paste operations took {} s".format(self.N, cut_paste_time_m4)) # string formatting & '+'
            cutList_stringformatting.append(cut_paste_time_m4)
            
            #========
            cut_paste_time_m5 = timeit.timeit(stmt=self.editor_cut_paste_m5, setup=new_editor, number=1)
            print("{} times [m5] cut paste operations took {} s".format(self.N, cut_paste_time_m5)) # assignment '+' & % operator
            pasteList_percent.append(cut_paste_time_m5)

            cut_paste_time_m6 = timeit.timeit(stmt=self.editor_cut_paste_m6, setup=new_editor, number=1)
            print("{} times [m6] cut paste operations took {} s".format(self.N, cut_paste_time_m6)) # assignment '+' & f-string
            pasteList_fstring.append(cut_paste_time_m6)

            cut_paste_time_m7 = timeit.timeit(stmt=self.editor_cut_paste_m7, setup=new_editor, number=1)
            print("{} times [m7/best] cut paste operations took {} s".format(self.N, cut_paste_time_m7)) # assignment '+' & str.join()
            pasteList_join.append(cut_paste_time_m7)

            cut_paste_time_m8 = timeit.timeit(stmt=self.editor_cut_paste_m8, setup=new_editor, number=1)
            print("{} times [m8] cut paste operations took {} s".format(self.N, cut_paste_time_m8)) # assignment '+' & str.format()
            pasteList_format.append(cut_paste_time_m8)

            copy_paste_time = timeit.timeit(stmt=self.editor_copy_paste, setup=new_editor, number=1)
            print("{} times [m0] copy paste operations took {} s".format(self.N, copy_paste_time))

            copy_paste_time_best = timeit.timeit(stmt=self.editor_copy_paste_best, setup=new_editor, number=1)
            print("{} times [best] copy paste operations took {} s".format(self.N, copy_paste_time_best))
            bestCopyList.append(copy_paste_time_best)

            get_text_time = timeit.timeit(stmt=self.editor_get_text, setup=new_editor, number=1)
            print("{} times [m0] text retrieval operations took {} s".format(self.N, get_text_time))

            misspellings_time = timeit.timeit(stmt=self.editor_misspellings, setup=new_editor, number=1)
            print("{} times [m0] misspelling operations took {} s".format(self.N, misspellings_time))
            

if __name__ == "__main__":
    for i in range(15): # num of operations loop thru 2^1 to 2^14
        b = EditorBenchmarker(["hello friends"], 2**i)
        timeslist.append(2**i)
        b.benchmark()
    
    #Figure 1: compare different Cut Operations
    plt.figure(figsize=(16, 4))
    plt.title("Figure 1: Different Cut Operations Comparison while using '+' as Paste Method")
    plt.plot(timeslist, cutList_assignment, 's-', color = 'r', label = "assignment '='") #red
    plt.plot(timeslist, cutList_copy, 'o-',  color = 'g', label = "copy.copy()") #green
    plt.plot(timeslist, cutList_deepcopy, '+-' , color = 'b', label = "copy.deepcopy()") #blue
    plt.plot(timeslist, cutList_pyperclip, 'p-',  color = 'y', label = "Pyperclip") #Yelloe
    plt.plot(timeslist, cutList_stringformatting, '*-' , color = 'c', label = "string formatting") #c
    plt.xlabel('Amount of Repeated Cut & Paste Operations')
    plt.ylabel('Time Spent (second)')    
    plt.legend(loc = "best")
    plt.show()

    #Figure 2: compare different Cut Operations (without pyperclip)
    plt.figure(figsize=(16, 4))
    plt.title("Figure 2: Different Cut Operations Comparison while using '+' as Paste Method (Without Pyperclip)")
    plt.plot(timeslist, cutList_assignment, 's-', color = 'r', label = "assignment '='") #red
    plt.plot(timeslist, cutList_copy, 'o-',  color = 'g', label = "copy.copy()") #green
    plt.plot(timeslist, cutList_deepcopy, '+-' , color = 'b', label = "copy.deepcopy()") #blue
    plt.plot(timeslist, cutList_stringformatting, '*-' , color = 'c', label = "string formatting") #c
    plt.xlabel('Amount of Repeated Cut & Paste Operations')
    plt.ylabel('Time Spent (second)')    
    plt.legend(loc = "best")
    plt.show()

    #Figure 3: compare different Cut Operations (without pyperclip or string formatting)
    plt.figure(figsize=(14, 4))
    plt.title("Figure 3: Different Cut Operations Comparison while using '+' as Paste Method (Without Pyperclip and String Formatting)")
    plt.plot(timeslist, cutList_assignment, 's-', color = 'r', label = "assignment '='") #red
    plt.plot(timeslist, cutList_copy, 'o-',  color = 'g', label = "copy.copy()") #green
    plt.plot(timeslist, cutList_deepcopy, '+-' , color = 'b', label = "copy.deepcopy()") #blue
    plt.xlabel('Amount of Repeated Cut & Paste Operations')
    plt.ylabel('Time Spent (second)')    
    plt.legend(loc = "best")
    plt.show()

    #==========================================================
    #Figure 4: compare different Paste Operations
    plt.figure(figsize=(16, 4))
    plt.title("Figure 4: Different Paste Operations Comparison while using Assignment '=' as Cut Method")
    plt.plot(timeslist, pasteList_plus, 's-', color = 'r', label = "'+'") #red
    plt.plot(timeslist, pasteList_percent, 'o-',  color = 'g', label = "%") #green
    plt.plot(timeslist, pasteList_fstring, '+-' , color = 'b', label = "f-string") #blue
    plt.plot(timeslist, pasteList_join, 'p-',  color = 'y', label = "str.join()") #Yelloe
    plt.plot(timeslist, pasteList_format, '*-' , color = 'c', label = "str.format()") #c
    plt.xlabel('Amount of Repeated Cut & Paste Operations')
    plt.ylabel('Time Spent (second)')    
    plt.legend(loc = "best")
    plt.show()

    #Figure 5: compare different Paste Operations (without f-string)
    plt.figure(figsize=(16, 4))
    plt.title("Figure 5: Different Paste Operations Comparison while using Assignment '=' as Cut Method (without f-string)")
    plt.plot(timeslist, pasteList_plus, 's-', color = 'r', label = "'+'") #red
    plt.plot(timeslist, pasteList_percent, 'o-',  color = 'g', label = "%") #green
    plt.plot(timeslist, pasteList_join, 'p-',  color = 'y', label = "str.join()") #Yelloe
    plt.plot(timeslist, pasteList_format, '*-' , color = 'c', label = "str.format()") #c
    plt.xlabel('Amount of Repeated Cut & Paste Operations')
    plt.ylabel('Time Spent (second)')    
    plt.legend(loc = "best")
    plt.show()

    #=======================
    #Figure 6: show best cut-paste performance: assignment '=' & str.join()
    plt.figure(figsize=(16, 4))
    plt.title("Figure 6: Show Best Cut-Paste Performance (using assignment '=' & str.join())")
    plt.plot(timeslist, pasteList_join,'s-', color = 'r') #red
    plt.xlabel('Amount of Repeated Cut & Paste Operations')
    plt.ylabel('Time Spent (second)')    
    for a, b in zip(timeslist, pasteList_join):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=5)
    plt.legend(loc = "best")
    plt.show()

    #Figure 7: show best copy-paste performance: assignment '=' & str.join()
    plt.figure(figsize=(16, 4))
    plt.title("Figure 7: Show Best Copy-Paste Performance (using assignment '=' & str.join())")
    plt.plot(timeslist, bestCopyList,'s-', color = 'r') #red
    plt.xlabel('Amount of Repeated Copy & Paste Operations')
    plt.ylabel('Time Spent (second)')    
    for a, b in zip(timeslist, bestCopyList):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=5)
    plt.legend(loc = "best")
    plt.show()

    # print("when we got the best combination, do some testing: ") # [m3] & [m6] should be commented out for this test
    # b = EditorBenchmarker(["hello friends"], 100000)
    # b.benchmark()