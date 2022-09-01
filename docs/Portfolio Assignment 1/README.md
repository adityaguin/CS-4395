## Text Processing with Python

### Assignment overview
The program reads in a data.csv (file location specified in the sysarg) containing employee data.
It takes the data, makes necessary modifications (described in the error messages in the program),
and then saves it into a employee dictionary (dictionary of persons). Then it saves the dictionary
into a dict.p file (in binary) using pickle, opens that file, reads that file, and prints the data
about each employee. 

### Running the program
The location of the data.csv must be provided in the second sysarg. Then run the program on terminal, makes the necessary changes as prompted. After, processing the data and populating the dictionary, the program will save the dictionary into a dict.p file, and then print the contents of that file.

### Python text processing

#### Strengths: 
Many methods already exist in libraries to process and modify text. Methods are fairly intuitive with regard to naming convention.

#### Weakness: 
Python is slower compared to languages such as C, C++. 

## What I learned

I learned of different python methods such as .capitalize() and .lower(). I also learned of different libraries such as pickle, csv, and regex. Regex took a bit of time to understand, but it was very useful for formatting. Data structures including dictionaries, lists, sets, list comprehension was also interesting to learn. 