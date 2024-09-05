# BasicBloomFilter
A basic Python Bloom filter implementation for free use

#Disclaimer
The text files in "\BasicBloomFilter\text_files\" are needed to run this program.
Do not change the file names.
Edit or overwrite as needed.
The current files are blank.

#How to Run:
To run the code in the terminal - 
Get to the code file directory:
.......\BasicBloomFilter\

In case of string errors, enclose the file address in double quotes (" ").

Execute command:
python basic_bloom_fil.py

Change dictionary.txt and loader.txt in "\BasicBloomFilter\text_files\" to change the dictionary values and loaded values.

#Setup and Optimization
Change variables "n_items" for the number of expected items and "f_pos_rate" for false positive rate requirement.
The built-in version is slow and low-error focused.
Please edit this to your needs.
The formula for false positive rate was taken from a medium article by Satish Mishra.
( https://techtonics.medium.com/implementing-bloom-filters-in-python-and-understanding-its-error-probability-a-step-by-step-guide-13c6cb2e05b7 )


The function "test_dictionary" outputs the stats to the terminal. 
Optimize and change this as per your needs.
This function is slow and can be improved greatly.

#Notes
Any feedback and interaction is greatly appreciated!
Thank you!
