# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:42:18 2018

@author: Shanshan
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:37:58 2018

@author: Shanshan
"""


import csv
import sys

#open file and read in data

def get_data(inputFile):
    #read in txt file,separate header and the body text
    with open(inputFile,'r') as f_in:
        next(f_in) # header line
        f_input = csv.reader(f_in)
        return list(f_input)

def process_count(data):
    count_dic = {}    # store counting data to a dictionary
    
    for line in data:
        prescriber_inline = line[1].lower() + line[2].lower()
        drug_name = line[3]
        drug_cost = float(line[4])

        if drug_name not in count_dic:            
            unique_prescriber = set([prescriber_inline])
            total_cost = drug_cost
            count_dic[drug_name] = [unique_prescriber, total_cost]
        else:
            exist_drug = count_dic[drug_name]
            exist_drug[0].add(prescriber_inline)
            exist_drug[1]+= drug_cost
    #    print(data)
    return count_dic
    

def process_data(result):
    tuples = []
    
    for drug in result:

        drug_info = result[drug]
        num_prescriber = len(drug_info[0])
        total_cost = drug_info[1]
        tuples.append((drug, num_prescriber, round(total_cost)))
        
    tuples.sort(key = lambda x:(-x[2],x[0]))

    return tuples
            
def write_output(file,result,output_header):
    with open(file, 'w') as f_out:
        f_ouput = csv.writer(f_out)
        f_ouput.writerows(output_header)
        f_ouput.writerows(result)
    
def main():
#    input_file = sys.argv[1]
#    output_file = sys.argv[2]
    input_file = 'itcont.txt'
    output_file = 'top_cost_drug.txt'
    #output_header follows the instuction
    output_header = [['drug_name','num_prescriber','total_cost']]
    
    data = get_data(input_file)
    result = process_count(data)
    output_text = process_data(result)
    write_output(output_file,output_text,output_header)
 #   print(data)
 #   print(result)
           
if __name__ == '__main__':
    main()
