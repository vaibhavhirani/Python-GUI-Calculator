def output(equation):
    import math
    #123+123
    oprn=[]
    oprt=[]
    for i in equation:
        if i=='+':
                #print("this is start of inner loop")
                a=[]
                oprt.append(i)
                a=equation.split('+',1)
                oprn.append(a[0])
                del a[0]
                #print(a)
                s=''
                equation=s.join(str(x) for x in a)
                '''print(equation)
                print(a)
                print("this is different")
                print(oprn)
                print(oprt)'''

        if i=='-':
                #print("this is different")
                a=[]
                oprt.append(i)
                a=equation.split('-',1)
                oprn.append(a[0])
                del a[0]
                s=''
                equation=s.join(str(x) for x in a)
                #print("this is different")
                '''print(equation)
                print(a)
                print(oprn)
                print(oprt)'''

        if i=='*':
                #print("this is different")
                a=[]
                oprt.append(i)
                a=equation.split('*',1)
                oprn.append(a[0])
                del a[0]
                s=""
                equation=s.join(str(x) for x in a)
                '''print("this is different")
                print(equation)
                print(a)'''

        if i=='/':
                #print("this is different")
                a=[]
                oprt.append(i)
                a=equation.split('/',1)
                oprn.append(a[0])
                del a[0]
                s=''
                equation=s.join(str(x) for x in a)
                '''print("this is different")
                print(equation)
                print(a)'''


    #print("Outside loop")
    oprn.append(str(equation))
   #print(oprn)
    #print(oprt)'''
    L=len(oprt)
    #DIVISION
    for i in range(0,L):
    
        if oprt[(L-1)-i]=='/':
            c=float(oprn[oprt.index('/')])/float(oprn[oprt.index('/')+1])
            oprn.insert(oprt.index('/'),c)
            del oprn[oprt.index('/')+1]
            del oprn[oprt.index('/')+1]
            del oprt[oprt.index('/')]
            #print(oprn)
            #print(oprt)
            
        else:
            continue
    L1=len(oprt)
    #MULTIPLICATION
    for i in range(0,L1):

        if oprt[(L1-1)-i]=='*':
            c=float(oprn[oprt.index('*')])*float(oprn[oprt.index('*')+1])
            oprn.insert(oprt.index('*'),c)
            del oprn[oprt.index('*')+1]
            del oprn[oprt.index('*')+1]
            del oprt[oprt.index('*')]
            #print(oprn)
            #print(oprt)
            
        else:
            continue
    #ADDITION AND SUBTRACTION
    L2=len(oprt)
    for j in range(0,L2):
        
        if oprt[0]=='+':
            c=float(oprn[0])+float(oprn[1])
            oprn.insert(0,c)
            del oprn[1]
            del oprn[1]
            del oprt[0]
            #print(oprn)
            #print(oprt)
            if(oprt==[]):
                break;

        if oprt[0]=='-':
            c=float(oprn[0])-float(oprn[1])
            oprn.insert(0,c)
            del oprn[1]
            del oprn[1]
            del oprt[0]
            #print(oprn)
            #print(oprt)
            #print("- ke bad")
            #print(j)
            if(oprt==[]):
                break;

    '''print("final answer is ")
    print(oprn[0])'''
    return oprn[0]
