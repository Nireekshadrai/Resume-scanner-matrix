def experience(res_dct,condition,field):
    if '>' in condition:
                            if ">=" in condition: 
                                print("enterered")
                                ndeg=condition.replace(">=", '').strip()
                                print(ndeg)
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())>=ndeg):
                                        print("enter2")
                                        return True
                                else:
                                    print("enter valid input")
                            else:
                                ndeg=condition.replace('>', '').strip()
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())>ndeg):
                                        return True
                                else:
                                    print("enter valid input")
    elif '<' in condition: 
                            if "<=" in condition: 
                                ndeg=condition.replace("<=", '').strip()          #string immutable in python
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())<=ndeg):
                                        return True
                                else:
                                    print("enter valid input")
                            else:
                                ndeg=condition.replace('<', '').strip()
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())<ndeg):
                                        return True
                                else:
                                    print("enter valid input")
    elif '=' in condition: 
                            ndeg=condition.replace('=', '').strip()
                            if ndeg.isdigit():
                                if((res_dct["total_exp"].strip())==ndeg):
                                    return True
                            else:
                                print("enter valid input")
                        
    else:
        print("invalid input for experience")