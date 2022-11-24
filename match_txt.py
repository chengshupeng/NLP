import os
path = 'txt'
fileName=[f for f in os.listdir(path) ]
def match_txt(input_file,output_file):
    txt = {}
    for i in range(len(fileName)):
        with open('txt/' + fileName[i], encoding='utf-8') as f:
            txt[i] = [w.strip() for w in f.read().split()]
        f.close()
    with open(input_file, encoding='utf-8') as f:
        words = [w.strip() for w in f.read().split('\n')]
    f.close()
    t = open(output_file, 'w+', encoding='utf-8')
    for K in range(len(words)-2):
        a=words[K]
        for j in range(len(fileName)-1):
            txts=txt[j]
            if a in str(txts):
                t.write(a)
                t.write(":")
                t.write(fileName[j])
                t.write("\n")

match_txt("three/three.txt","three/result_2.txt")
match_txt("four/four.txt","four/result_2.txt")
match_txt("five/five.txt","five/result_2.txt")
match_txt("six/six.txt","six/result_2.txt")
match_txt("seven/seven.txt","seven/result_2.txt")
match_txt("one/one.txt","one/result_2.txt")

match_txt("two/two_tre.txt","two/result_3.txt")
match_txt("three/three_tre.txt","three/result_3.txt")
match_txt("four/four_tre.txt","four/result_3.txt")
match_txt("five/five_tre.txt","five/result_3.txt")

path_one = 'one/one_tre'
OneName=[f for f in os.listdir(path_one) ]
txt={}
for u in range(len(OneName)):
    match_txt("one/one_tre/"+OneName[u],"one/one_tre/result_3"+ "_001" +".txt")
