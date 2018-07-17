# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:37:58 2018

@author: Shanshan
"""


import csv
import sys

#open file
    
def get_data(file):
    #read in txt file line by line,separate header and the body text
    with open(file,'r') as f_in:
        f_input = csv.reader(f_in)
        next(f_input)
       # header = next(f_input)
       #0: id, 1: last name, 2: first name, 3: drug name, 4: cost
        return list(f_input)

def process_count(data):
    #process the counting, return aggregated list with each durg is a single entry
    #along with the number of prescirbers and total cost
    f_output = []
    temp_drug = []
    temp_prescriber = []
    temp_num_prescriber = []
    temp_cost = []
    
    for line in data:
        #0: id, 1: last name, 2: first name, 3: drug name, 4: cost
        prescriber_inline = line[1]+line[2]
#        print(line)
#        print(f_output)
        if line[3] == temp_drug:
            temp_cost += float(line[4])
            if prescriber_inline != temp_prescriber:
                temp_num_prescriber +=1
        else:
            
            if temp_drug:
                f_output.append([temp_drug,temp_num_prescriber,round(temp_cost)])
              #  f_output.append('\n')
               
            temp_drug = line[3]
            temp_cost = float(line[4])
            temp_prescriber = prescriber_inline
            temp_num_prescriber = 1
    f_output.append([temp_drug,temp_num_prescriber,round(temp_cost)])
    f_output.sort(key = lambda x:(-x[2],x[0]))
    return f_output
    
def write_output(file,result,output_header):
    with open(file, 'w',newline='') as f_out:
        f_ouput = csv.writer(f_out)
        f_ouput.writerows(output_header)
        f_ouput.writerows(result)
    
def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
#    input_file = 'itcont.txt'
#    output_file = 'top_cost_drug.txt'
    output_header = [['drug_name','num_prescriber','total_cost']]
    
    data = get_data(input_file)
    result = process_count(data)
    write_output(output_file,result,output_header)
    print(data)
    print(result)
        
    
if __name__ == '__main__':
    main()