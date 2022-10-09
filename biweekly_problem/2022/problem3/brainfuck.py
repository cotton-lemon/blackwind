import sys
def brainfuck(string):
    memory=[0]*10000
    pointer=0
    idx=0
    n=len(string)
    while idx<n:
        t=string[idx]
        if t=='>':
            pointer+=1
        elif t=='<':
            pointer-=1
        elif t=='+':
            memory[pointer]+=1
        elif t=='-':
            memory[pointer]-=1
        elif t=='.':
            sys.stdout.write(chr(memory[pointer]))
        elif t==',':
            memory[pointer]=int(input())
        elif t=='[':
            if memory[pointer]==0:
                need=1
                while need>0:
                    idx+=1
                    tt=string[idx]
                    if tt=='[':
                        need+=1
                    elif tt==']':
                        need-=1
                    
                        
        elif t==']':
            if memory[pointer]!=0:
                need=1
                idx-=1
                while need>0:
                    idx-=1
                    tt=string[idx]
                    if tt=='[':
                        need-=1
                    elif tt==']':
                        need+=1
        idx+=1

if __name__=="__main__":
    string="++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
    brainfuck(string)
    string="+++++++++++>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]"
    print('fibonacci from http://esoteric.sange.fi/brainfuck/bf-source/prog/fibonacci.txt')
    #from
    #http://esoteric.sange.fi/brainfuck/bf-source/prog/fibonacci.txt
    brainfuck(string)
    
