# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:37:58 2018

@author: Shanshan
"""


#import csv
import sys

#open file
    
def get_data(file):
    #read in txt file line by line,separate header and the body text
    with open(file,'r') as f_input:
        header = next(f_input)
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
        prescriber_inline = line[1]+' '+line[2]
        if line[3] == temp_drug:
            temp_cost += float(line[4])
            if prescriber_inline != temp_prescriber:
                temp_num_prescriber +=1
        else:
            
            if temp_drug:
                f_output.append([temp_drug,temp_num_prescriber,round(temp_cost,2)])
               
            temp_drug = line[3]
            temp_cost = float(line[4])
            temp_prescriber = prescriber_inline
            temp_num_prescriber = 1
    f_output.append([temp_drug,temp_num_prescriber,round(temp_cost,2)])
    f_output.sort(key = lambda x:(-x[2],x[0]))
    return f_output
    
def write_output(file_output,result,output_header):
    with open(file_output, 'w') as f_output:
        f_output.write(output_header)
        f_output.write(result)
    
def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    output_header = 'drug_name,num_prescriber,total_cost\n'
    
    data = get_data(input_file)
    result = process_count(data)
    write_output(output_file,result,output_header)
        
    
if __name__ == '__main__':
    main()