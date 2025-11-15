def write_number_grid(path:str, m:int, n:int):
    matrix = [[] for i in range(m)] # [[],[],[],[],[]]
    for i in range(0,m*n):
        # 0//3 = 0
        # 1//3 = 0
        matrix[i//n].append(str(i+1))
    
    string_matrix = [" ".join(row) for row in matrix]

    with open(path,"w") as file:
        file.write( "\n".join(string_matrix))
   

from datetime import datetime
def log_message(filename:str,s2:str):
  with open(filename,"a") as file:
    file.write(f"{datetime.now()} - {s2}" + "\n")


dict={}
def read_config(filename: str):
  with open(filename,"r") as file:
    for line in file:
      s1,s2=line.strip().split("=")
      dict[s1]=s2
    return dict   

def write_config(filename,dict):
  with open(filename,"w") as file:
     for key,val in dict.items():
        file.write(f"{key}={val}\n")

def find_and_replace(input_file,output_file,old_word,new_word):
  with open(input_file,"r")as file , open(output_file,"w") as f:
    file_content=file.read()
    update_content=file_content.replace(old_word,new_word)
    f.write(update_content)
