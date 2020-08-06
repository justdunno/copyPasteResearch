import pyperclip as pc 

class SimpleEditor:
    def __init__(self, document):
        self.document = document
        self.dictionary = set()
        with open("/wft/filesfrom/file1.txt") as input_dictionary: #"/wft/ncsu/dict/words"
            for line in input_dictionary:
                words = line.strip().split(" ")
                for word in words:
                    self.dictionary.add(word)
        self.paste_text = ""

    def cut(self, i, j): #original cut method
        self.paste_text = self.document[i:j]
        self.document = self.document[:i] + self.document[j:]

    def copy(self, i, j): #original copy method
        self.paste_text = self.document[i:j]

    def paste(self, i): #original paste method
        self.document = self.document[:i] + self.paste_text + self.document[i:]
        #print("paste_text: " + self.paste_text)

    
    def copy_paste_using_pyperclip(self, i, j, k):
        pc.copy(self.document[i:j]) # copying text to clipboard 
        self.document = self.document[:k] + pc.paste() + self.document[k:] #paste text from clipboard  to k position

    def get_text(self):
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

    #first cut then paste
    editor_cut_paste = """
for n in range({}):
    if n%2 == 0: 
        s.cut(1, 3)
    else:
        s.paste(2)"""

    editor_copy_paste = """
for n in range({}):
    if n%2 == 0:
        s.copy(1, 3)
    else:
        s.paste(2)"""

    #===== method 1 : using copy_paste_using_pyperclip(self, i, j) ===========
    editor_copy_paste_m1 = """
for n in range({}):
    if n%2 == 0:
        s.copy_paste_using_pyperclip(1, 3, 2)"""

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
        self.editor_copy_paste = self.editor_copy_paste.format(N)
        self.editor_copy_paste_m1 = self.editor_copy_paste_m1.format(N)
        self.editor_get_text = self.editor_get_text.format(N)
        self.editor_misspellings = self.editor_misspellings.format(N)

    def benchmark(self):
        for case in self.cases:
            print("Evaluating case: {}".format(case))
            new_editor = self.new_editor_case.format(case)

            cut_paste_time = timeit.timeit(stmt=self.editor_cut_paste, setup=new_editor, number=1)
            print("{} [m0] cut paste operations took {} s".format(self.N, cut_paste_time))

            copy_paste_time = timeit.timeit(stmt=self.editor_copy_paste, setup=new_editor, number=1)
            print("{} [m0] copy paste operations took {} s".format(self.N, copy_paste_time))

            copy_paste_time_m1 = timeit.timeit(stmt=self.editor_copy_paste_m1, setup=new_editor, number=1)
            print("{} [m1] copy paste operations took {} s".format(self.N, copy_paste_time_m1))

            get_text_time = timeit.timeit(stmt=self.editor_get_text, setup=new_editor, number=1)
            print("{} [m0] text retrieval operations took {} s".format(self.N, get_text_time))

            misspellings_time = timeit.timeit(stmt=self.editor_misspellings, setup=new_editor, number=1)
            print("{} [m0] misspelling operations took {} s".format(self.N, misspellings_time))
            

if __name__ == "__main__":
    b = EditorBenchmarker(["hello friends"], 10)
    b.benchmark()