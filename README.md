# Research on Cut/Copy/Paste TextEditor

## a. How to run the program.

1. Install External Library: \
External library used: pyperclip \
Installing pyperclip:
    ```
    pip install pyperclip
    ```

2. Then, go to the directory of editor.py. On terminal, type the below text to run the program:
    ```
    python editor.py
    ```
    
*Note: sometimes, it may take about 10s for tedious some methods used in the program, such as pyperclip*

===========================================================================
## b. My high level approach to the problem.

### Basic Ideas:

For the original copy/cut/paste methods in the given code, we can see that all the operations are based on manipulating the strings:

*Cut & Paste*: **save and remove** a part of string using *self.document[i:j]* to get string's ith character to jth character (jth is not included); put the saved substring into a string using *+* operation such as *self.document[:i] + self.paste_text + self.document[i:]*

*Copy & Paste*: **save** a part of string using *self.document[i:j]* to get string's ith character to jth character (jth is not included);
put the saved substring into a string using *+* operation such as *self.document[:i] + self.paste_text + self.document[i:]*

According to the code and the definition, there are two steps of the cut-paste/copy-paste operation; thus, the trial of speeding up the cut/copy/paste operations can focus on both speeding up **copy/cut operations** and **paste operations (Python String Concatenation)**. 

****
For Cut/Copy operations, I need to rank some methods by its performance. Methods include: \
- **1). Use Assignment Operator '=' to get to-be-paste text (original code: )** \
    By using assignment operator, the memory address (pointer) get assigned to the new variable and get saved by it. 
    It is a way of shallow copy.
    ```
    For example, if *a = [1, 2, 3]* and then we do *b = a*, b and a would both point to the same memory address.
    When we alter a to be *"a.append(4)"*, then we would have both *"a = [1, 2, 3, 4]"* and *"b = [1, 2, 3, 4]"*
    ```
- **2). Use copy.copy() for shallow copy** \
    Both assignment operator and copy.copy() are the ways of shallow copy. 
    ```
    However, for example, if a is a compound object *a = [1, 2, 3]* and then we do *b = copy.copy(a)*, object b and object a would not refer to the same address, but their elements, say a[0] and b[0] are still pointing to the same memory address
    Still, when we alter *"a"* to be *"a.append(4)"*, then we would have both *"a = [1, 2, 3, 4]"* and *"b = [1, 2, 3, 4]"*.
    ```

- **3). Use copy.deepcopy() for deep copy** \
    Deep copy method make sure the old contents are inserted into the new variable while the new variable is being constructed. 
    ```
    For example, if a is a compound object *a = [1, 2, 3]* and then we do *b = copy.deepcopy(a)*, object b and object a would refer to the different addresses.
    When we alter *"a"* to be *"a.append(4)"*, then we would have *"a = [1, 2, 3, 4]"* and still *"b = [1, 2, 3]"*.
    ```

- **4). Use pyperclip to copy desired content into clipboard** \
    To-be-pasted content is store on the computer' clipboard using *pyperclip.copy()*, and would be retrieved while doing paste operation using *pyperclip.paste()*. 

- **5). Use string formatting for shallow copy** \
    It is also a way of shallow copy. The syntax would be *b = '%s' % a[i:j]*

 
For Paste operations (Python String Concatenation), I need to rank some methods by its performance as well. Methods include:
- **1). Use '+' for string concatenation** \
    Using the '+' operator is what the original code does. All the elements to be concatenated using '+' must be strings.

- **2). Use '%' for string concatenation** \
    Using the '%' operator is also a straightforward way for string concatenation, and it can also help with formatting.  

- **3). Use f-string for string concatenation** \
    f-string is a python 3 improvement method on %-formatting, it makes the syntax of string-concatenation code more readable.

- **4). Use str.join() method for string concatenation** \
    join() method accepts list parameter, and can combine string elements in the list together.

- **5). Use str.format() method for string concatenation** \
    format() method is a positional format method to concatenate elements including strings, characters, integers, etc. together.


===========================================================================
## c. Experiments & Results:

Since the cut operation includes *1). extract the according text; 2). deleted this text; 3). paste and insert it back* and the copy operation includes *1). extract the according text; 2). paste and insert it back*, then we can do experiments only on the cut-paste operation to test different methods mentioned above.

The number of repeated operations is looped through 2^0 = 1, 2^1 = 2, 2^2 = 4, ..., 2^14 = 16384. Line charts would be created using *matplotlib.pyplot* to show the performances of different methods' combination. 

- To compare different cut/copy methods, below is what we need to compare together (since "cut operation" includes "copy "):

    **Method 0 (the original method)**: Use *assignment '='* for cut operation and *'+'* for string concatenation

    **Method 1**: Use *copy.copy() (shallow copy)* and *'+'* for string concatenation

    **Method 2**: Use *copy.deepcopy()* for cut/copy operation and *'+'* for string concatenation

    **Method 3**: Use external module *Pyperclip* for cut/copy operations and *'+'* for string concatenation

    **Method 4**: Use *string formatting (shallow copy)* for cut/copy operations and *'+'* for string concatenation

    Using all the information above, line charts can be created from it. 

    Figure 1: 
    ![image](https://github.com/justdunno/PicsForMyReadmes/blob/master/Figure_1.png) 

    According to the Figure 1 above, the pyperclip method clearly cost the much more time than other methods because it access the computer's clipboard each time for putting text into it and retrieving text from it. Additionally, if we use pyperclip method for too many times, it would prevent users from using clipboard features correctly for doing other things since the clipboard is constantly occupied by this cut/paste method. However, if we only need to do a small amount (1-10) of repeated cut-paste or copy-paste operations, using clipboard (pyperclip method) can be faster than using other methods.

    Figure 2:
    ![image](https://github.com/justdunno/PicsForMyReadmes/blob/master/Figure_2.png) 
    
    According to the Figure 2 above, we can see that there is still a method, String Formatting, clearly cost more time than other methods. Then we can get rid of this line and create the chart again.

    Figure 3: 
    ![image](https://github.com/justdunno/PicsForMyReadmes/blob/master/Figure_3.png)

    According to the Figure 3 above, when there are only Assignment '=', copy.copy(), copy.deepcopy() methods left, we can clearly see that generally, when the repeat time goes up, Assignment method has the best performance among them all. Note: Sometimes, copy.copy() can get better performance than using Assignment; it may because both of them are shallow copy method. The difference usually would not be larger than 0.001s when the repeated time is 16,384. 


****
- To compare different paste methods, below is what we need to compare together (we use ):

    **Method 0 (the original method)**: Use *assignment '='* for cut operation and *'+'* for string concatenation

    **Method 5**: Use *assignment '='* and *'%'* for string concatenation

    **Method 6**: Use *assignment '='* and *f-string* for string concatenation

    **Method 7**: Use *assignment '='* and *str.join()* for string concatenation

    **Method 8**: Use *assignment '='* and *str.format()* for string concatenation

    Figure 4: 
    ![image](https://github.com/justdunno/PicsForMyReadmes/blob/master/Figure_4.png) 

    According to the Figure 4 above, f-string method has clearly much worse performance compared to others, so we can remove this line to see the line chart more clearly.

    Figure 5:
    ![image](https://github.com/justdunno/PicsForMyReadmes/blob/master/Figure_5.png) 

    According to the Figure 5 above, the paste method str.join() has the best performance among all the paste (string concatenation) methods. Note: sometimes, '+' operator can defeat str.join()'s performance. However, the time spent difference between str.join() and '+' method would not get larger than 0.0001s.

****
- To sum up, the cut/copy method *assignment '='* and the paste method *str.join()* have the best performance. So I tried to get the time spent data of this best combination:

    Figure 6:
    ![image](https://github.com/justdunno/PicsForMyReadmes/blob/master/Figure_6.png) 

    According to the Figure 6, the *16,384 (2^15)* repeated cut-paste operations can only take about **0.0064** seconds. Approximately, this method improves the cut-paste performance by around *7.2%* compared to the original cut-paste method (takes average 0.0069 in average). 

    When I commented out the pyperclip method and tried to run more times. I got about 0.05 seconds run-time for 100,000 repeated cut-pated operations using assignment '=' and str.join().

    Figure 7:
    ![image](https://github.com/justdunno/PicsForMyReadmes/blob/master/Figure_7.png) 

    According to the Figure 7, the *16,384 (2^15)*  repeated copy-paste operations can only take about **0.0082** seconds. Approximately, this method improves the cut-paste performance by around *20.8%* compared to the original copy-paste method (takes around 0.00997 in average). 

    When I commented out the pyperclip method and tried to run more times. I got about 0.13 seconds run-time for 100,000 repeated cut-pated operations using assignment '=' and str.join().

===========================================================================
## d. Any extensions you have added or would like to add if you had more time.

For this project, I have tried to use as many ways of cut/copy operation and paste operation as possible to cover all the methods to find the best combination of cut/copy operation and paste operation according to their performances. I have added "pyperclip" library to the project while implementing cut/copy operation because this library can support clipboard operations on Windows/MacOs/Linux. 
    
The project could be easier to operate if a well-designed GUI is added to it. Additionally, there are other reasons can affect the final performance, such as to-be-pasted text's length and so on. Due to the limited time, I did not get to do experiments on the impact that to-be-pasted text's length could have on the performance. 

