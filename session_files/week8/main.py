# def write_number_grid(path:str, m:int, n:int):
#     matrix = [[] for i in range(m)] # [[],[],[],[],[]]
#     for i in range(0,m*n):
#         # 0//3 = 0
#         # 1//3 = 0
#         matrix[i//n].append(str(i+1))
    
#     string_matrix = [" ".join(row) for row in matrix]

#     with open(path,"w") as file:
#         file.write( "\n".join(string_matrix))
   

# from datetime import datetime
# def log_message(filename:str,s2:str):
#   with open(filename,"a") as file:
#     file.write(f"{datetime.now()} - {s2}" + "\n")


# dict={}
# def read_config(filename: str):
#   with open(filename,"r") as file:
#     for line in file:
#       s1,s2=line.strip().split("=")
#       dict[s1]=s2
#     return dict   

# def write_config(filename,dict):
#   with open(filename,"w") as file:
#      for key,val in dict.items():
#         file.write(f"{key}={val}\n")

# def find_and_replace(input_file,output_file,old_word,new_word):
#   with open(input_file,"r")as file , open(output_file,"w") as f:
#     file_content=file.read()
#     update_content=file_content.replace(old_word,new_word)
#     f.write(update_content)

# def summarize_sales(inp:str, out:str):
#   with open(inp, 'r') as file:
#     d = {}
#     for sales_str in file.readlines():
#       word,value = sales_str.split()
#       if word in d.keys():
#         d[word] += int(value)
#       else:
#         d[word] = int(value)
#   sort = sorted(d)
#   print(sort)
#   with open(out, 'w') as file:
#     for key in sort:
#       file.write(f"{key}: {d[key]}\n")


# summarize_sales("sales.txt","summary.txt")

# def parse_indented_list(inp:str, out:str):
#   count = 0
#   project = ""
#   with open(inp, 'r') as file,open(out, 'w') as file2:
#     lines = file.readlines()
#     for line in lines:
#       line = line.rstrip()
#       if line.startswith('  '):
#         count += 1
#       else:
#         if project:
#           file2.write(f'{project}: {count} tasks\n')
#         project = line
#         count = 0
#     file2.write(f'{project}: {count} tasks\n')
#   # with open(out, 'w') as file:
#   #   file.write(f'{project} = {count}\n')
# parse_indented_list("projects.txt","summary.txt")
