import os
import condition_checker
condition=[]

def scanner(data,choice,path):
                result=[]

                for text in os.listdir(path):
                    
                    global res
                    resume1=open(path+text,"r")
                    resume2=resume1.read().splitlines() 
                    resume3=[i.split(":") for i in resume2]
                    for i in resume3:
                        if i==" ":
                            resume3.remove(i)
                    res_dct = {resume3[i][0]: resume3[i][1] for i in range(0, len(resume3), 1)}
                    count=0
                    
                    for i in range(len(choice)):
                        print(data[i])
                        print(choice[i])
                        res=condition_checker.check_condition(res_dct,data[i],choice[i])
                        print("res ",res)
                        
                                    
                        
                        if res=="-1":
                                result.append("invalid")
                                return result
                        elif res:
                                count=count+1
                                print(text,count)                
                                    
                                    
                    if count==len(choice):
                        result.append(text)
                
                    
                return result
                
                


