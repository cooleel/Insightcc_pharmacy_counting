# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:42:18 2018

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
        '''prescriber name, drug_name and drug_cost inline'''
        prescriber_inline = line[1].lower() + line[2].lower()
        drug_name = line[3]
        drug_cost = float(line[4])

        if drug_name not in count_dic:  # new drug
            #check key(drug_name) of the count_dictionary
            unique_prescriber = set([prescriber_inline])
            #get new prescriber name
            total_cost = drug_cost
            #single entry of a new drug_name
            count_dic[drug_name] = [unique_prescriber, round(total_cost)]
        else:
            #update existing drug in dictionary
            exist_drug = count_dic[drug_name]
            exist_drug[0].add(prescriber_inline)
            exist_drug[1] += drug_cost

    return count_dic

# turn dictionary to data table
def process_data(result):
    lists = []

    for drug in result:

        drug_info = result[drug]  #get prescriber and cost value
        num_prescriber = len(drug_info[0])
        total_cost = drug_info[1]
        lists.append((drug, num_prescriber, int(total_cost)))

    #sort output first by cost then by drug name
    lists.sort(key = lambda x:(-x[2],x[0]))

    return lists

def write_output(file,result,output_header):
    with open(file, 'w') as f_out:
        f_ouput = csv.writer(f_out)
        f_ouput.writerows(output_header) #first add the header
        f_ouput.writerows(result)      #write in result table

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
#    input_file = 'itcont1.txt'
#    output_file = 'top_cost_drug1.txt'
    #output_header follows the instuction
    output_header = [['drug_name','num_prescriber','total_cost']]

    data = get_data(input_file)  #get data from input
    result = process_count(data) #get the count dictionary
    output_text = process_data(result) #get the count table from dictionary
    write_output(output_file,output_text,output_header)

if __name__ == '__main__':
    main()
