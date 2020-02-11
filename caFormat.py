#!/usr/bin/env python
# coding: utf-8

# # Converting Toolbox txt files to Common Separated Values (csv) files for Conversation Analysis
# This code was written by Sarah Moeller, University of Colorado Boulder on February 7, 2020. sarah.moeller@colorado.edu. 
# 
# This code was originally made for Irina Wagner who needed to quickly convert Arapaho data in order to conduct conversation analysis for her dissertation.
# 
# _Instructions to run code at bottom of file._

# ## Source Code 

# In[149]:


import os


# In[150]:


def removeSpaces(toolboxline):
    # multiple spaces -> one space
    # spacehyphen >> hyphen
    # hyphenspace -> hyphen
    
    toolboxline = toolboxline.replace(',', ' ')
    toolboxline = ' '.join(toolboxline.split())
    toolboxline = toolboxline.replace(' -', '-')
    toolboxline = toolboxline.replace('- ', '-')
    
    return toolboxline
    


# In[154]:


def toolbox2CA(filename):
    '''Reformats Irina's toolbox txt files.
    Writes to csv file'''
    
    NEWFILE = filename.split('.')[0] + '.csv'
    newlines = ''
    newline = ''
    anonymized = {'1': 'Margaret', '2': 'Joy', '3': 'Robert', '4': 'Sandra', '5': 'Bill', 
                  '6': 'John', '7': 'David', '8': 'Barb', '10': 'Mark', '11': 'Carol', '12': 
                  'Judy', '13': 'Betty', '14': 'Nancy', '15': 'Sharon', '16': 'Philip', 
                  '17': 'Linda', '18': 'Sam', '19': 'Timothy', '20': 'Martha', '21': 'Patricia', 
                  '22': 'Kathy', '23': 'Shirley', '24': 'Karen', '25': 'Phyllis', '26': 'Joyce', 
                  '27': 'Ann', '28': 'Albert', '29': 'Gloria', '30': 'Michael', '31': 'Alice', 
                  '32': 'Dennis', '33': 'Joe', '34': 'Ray', '35': 'Gary', '36': 'Steve', 
                  '37': 'Donna', '38': 'Virginia', '39': 'Doris', '40': 'Richard', '41': 'Elaine',
                  '42': 'Bonny', '44': 'Carla', '45': 'Larry', '46': 'Dan', '47': 'Peter', 
                  '48': 'Ronny', '49': 'George', '50': 'Donald', '51': 'Jerry', '52': 'Tom', 
                  '53': 'Sue', '54': 'Bruce', '55': 'Douglas', '56': 'Terry', '57': 'Roger', 
                  '58': 'Debbie', '59': 'Henry', '60': 'Frank', '61': 'Carla', '62': 'Researcher',
                  '63': 'Arthur', '64': 'Brenda', '65': 'Walter', '66': 'Willie', '67': 'Greg', 
                  '68': 'Marilyn', '69': 'Glenn', '70': 'Janice', '71': 'Peggy', '72': 'Fred', 
                  '73': 'Helen', 'XXX':'unknown', 'noid':'unknown'}
    
    inF = open(filename)
    lines = inF.readlines()
    inF.close()
    
    for line in lines[3:]:
        line = removeSpaces(line)
        # get the turn ID
        if line.startswith('ref'):
            linesplit = line.strip().split('.')
            newline = linesplit[-1] + ','
        # get name ID and original sentence
        elif line.startswith('tx@'):
            nameID = line.split()[0].split('@')[1]
            orgSent = ','.join(line.split()[1:])
            newline += anonymized[nameID] 
            newline += ':,' + orgSent + '\n'
        # get glosses, separated by comma
        elif line.startswith('ge@') or line.startswith('mb@') or line.startswith('ps@'):
            items = ','.join(line.split()[1:])
            newline += ',,' + items + '\n'
        # get free translation
        elif line.startswith('ft@'):
            newline += ',,' + ' '.join(line.split()[1:]) + '\n'
        # get silence ID
        elif line.startswith('SD'):
            newline += ',,' + ''.join(line.split()[-1]) + '\n'
        # new line between turns
        else:
            newline += '\n'
            newlines += newline
            newline = ''
    with open(NEWFILE, 'w') as NF:
        NF.write(newlines)
    #return newlines


# # To Run Code
# 1) Change path to directory if files are in different directory than this code file. Change replacing ./ with the path to new directory. If the files are in the same folder as this code file, use directory = r'./'.
# 
# 2) Make sure all files that need converting have the extension: .txt.
# 
# 3) Run code below. It will print out the name of all files that it didn't convert to csv. The CSV files will be saved in same folder.

# In[152]:


directory = r'./'
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        toolbox2CA(filename)
    else:
        print(os.path.join(directory, filename))

