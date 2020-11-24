import hashlib 

from threading import Thread
from multiprocessing import Process
from numba import cuda

from datetime import datetime
import string
import time
import os

# tenta fazer backup dos resultados caso ja tenham sido gerados
# usa o timestamp para gerar um backup unico
try:
    os.system("cp ./hashes_cuda.csv ./hashes_cuda_BKUP%s.csv"%(datetime.timestamp(datetime.now())))

except:
    pass

out = open("./hashes_cuda.csv","w") # cria um arquivo para armazenar as chaves descriptografadas 

out.write("HASH MD5,SENHA\n") # escreve um cabeçalho no arquivo

out.close()

'''
hashlist = ["81dc9bdb52d04dc20036dbd8313ed055",
"e2fc714c4727ee9395f324cd2e7f331f",
"3a4d92a1200aad406ac50377c7d863aa",
"912e79cd13c64069d91da65d62fbb78c",
"aff5ce2ec4cef26a63d1cf772e29f5ac",
"0a27bb4f7d32126e27dd5bbea4dbc2d4",
"81dc9bdb52d04dc20036dbd8313ed055",
"e2fc714c4727ee9395f324cd2e7f331f",
"3a4d92a1200aad406ac50377c7d863aa",
"912e79cd13c64069d91da65d62fbb78c",
"aff5ce2ec4cef26a63d1cf772e29f5ac",
"0a27bb4f7d32126e27dd5bbea4dbc2d4"]
'''
hashlist = ["82c8a24e125df09ce18906eda3e25062",
"59275c0a57c1912eba3b237d2bc57d6c",
"dd1df27fef89eb9b0364c3803fcf4ceb",
"47cb7cc4c1d3c8a0eb2afb5f9ce64377",
"5c281ef353b00703e224fae631403440",
"c46901272edfbe7730df9ff09518edb2",
"04b78196fdc6ffe443618571deb25846",
"a7af447f4133a73d3418fda6e650fcd3",
"29733d63917ebcda6c88ba69da1b25a2",
"eb9b0daccbff5f6be60d241263720955",
"95650081a595315bd36c2801f2c120af",
"c5dd4880f4aa1d623f28651afec2ed4a",
"751c39690fb8071c7292776d7b6a638f",
"6c066f396461ba8831088bcf8c2e8c19",
"b5197cebb685d19c1ffab146e9125783",
"6eba2afd08b788a46def38c420580240",
"0978496b93e1071dc7c40a81e95c3925",
"742e6fde3ea050e413ee491f0290354a",
"50aea0edbb9c8b91a810ad7f2e90b568",
"07208f17a430a235ceefc8a856b57f56",
"42c76757ae2b89a1ae9e7d3f2f918aac",
"c1491ad8c03e2ada58d3e7d773041723",
"8b365f0fd77f4a8b29b22fa9b3f46d2c",
"f649f3c248152f0e43638ac6cbc06594",
"8215e46a79498744224eb239cf100dc2",
"c5781aa76d4e4315f09f1c2c5afa04a8",
"8d9a372b47cf443cac9f097420538f05",
"61650746431e6c31ae845520b2a69ea2",
"d69e23084c0be871c5f95ed2ead45ffc",
"bb88750177831cffc8745005f7d1e253"]


# criação da lista com os seguintes caracteres: [ a-z/A-Z ],[ 0-9 ],[ !@#$%&*()_-+=[]{}?/\|>< ]

alph = ["!","@","#","$","%","&","*","(",")","_","-","+","=","[","]","{","}","?","/","\\","|",">","<"]

alph.extend(list(string.ascii_letters)) # extende a lista com as letras [ a-z/A-Z ]
alph.extend(list(string.digits)) # extende a lista com os numeros [ 0-9 ]

# função que percorre o alfabeto e testa cada palavra
@cuda.jit
def percorre(i):
    for x in alph:
        for y in alph:
            for z in alph:
                for a in alph:
                    for b in alph:
                        for c in alph:
                            for d in alph:
                                '''
                                teste4 = "%s%s%s%s"%(a,b,c,d)
                                resultado4 = (hashlib.md5(teste4.encode())).hexdigest()

                                if resultado4 == i:
                                    out = open("./hashes.csv","a") # cria um arquivo para armazenar as chaves descriptografadas 
                                    resultado = resultado4 + "," + teste4 + "\n"
                                    print(resultado)
                                    out.write(resultado)
                                    out.close()
                                    return(resultado)
                                '''
                                teste5 = "%s%s%s%s%s"%(z,a,b,c,d)
                                resultado5 = (hashlib.md5(teste5.encode())).hexdigest()

                                if resultado5 == i:
                                    out = open("./hashes.csv","a") # cria um arquivo para armazenar as chaves descriptografadas 
                                    resultado = resultado5 + "," + teste5 + "\n"
                                    print(resultado)
                                    out.write(resultado)
                                    out.close()
                                    return(resultado)
                                
                                teste6 = "%s%s%s%s%s%s"%(y,z,a,b,c,d)
                                resultado6 = (hashlib.md5(teste6.encode())).hexdigest()

                                if resultado6 == i:
                                    out = open("./hashes.csv","a") # cria um arquivo para armazenar as chaves descriptografadas 
                                    resultado = resultado6 + "," + teste6 + "\n"
                                    print(resultado)
                                    out.write(resultado)
                                    out.close()
                                    return(resultado)
                                
                                teste7 = "%s%s%s%s%s%s%s"%(x,y,z,a,b,c,d)
                                resultado7 = (hashlib.md5(teste7.encode())).hexdigest()

                                if resultado7 == i:
                                    out = open("./hashes.csv","a") # cria um arquivo para armazenar as chaves descriptografadas 
                                    resultado = resultado7 + "," + teste7 + "\n"
                                    print(resultado)
                                    out.write(resultado)
                                    out.close()
                                    return(resultado)
                    
                    '''
                    print(teste4)
                    print(resultado4)
                    time.sleep(1)
                    '''
                #print(teste5)


for i in hashlist:
    percorre()
    
    #t = Thread(target=percorre, args=(i,))
    #t.start()

'''
for i in range(len(hashlist)):
    p1 = Process(target=percorre, args=(hashlist[i], ))
    p1.start()
    # p1.join()
'''