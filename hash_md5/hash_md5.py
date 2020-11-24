import hashlib 

import threading
import multiprocessing

from datetime import datetime
from math import floor
import string
import time
import os

cores = 6 # 6

# tenta fazer backup dos resultados caso ja tenham sido gerados
# usa o timestamp para gerar um backup unico
try:
    os.system("mv ./hashes.csv ./hashes_BKUP%s.csv"%(datetime.timestamp(datetime.now())))
except:
    pass

out = open("./hashes.csv","w") # cria um arquivo para armazenar as chaves descriptografadas 

out.write("HASH MD5,SENHA\n") # escreve um cabeçalho no arquivo

out.close()

hashlist = ["6a4120be23c814f80233ecbb34e71adc",#p2
"728319765cfd5ffe1cec03aa66546d72",
#"ab4171e8d0d1a51a9c42e796ccdc0f03",#5
#"6cf444e98d01f65319755c6f3b3da28a",#5
"9eb0c9605dc81a68731f61b3e0838937",
"3f25a2fa7c6fa55849e6b54d2fe85897",
#"0a3c661fbd5ead8ed0f5a4034c6ddd84",#5
#"0382b5018951792285a5ed63d0d14758",#5
"86241b5767f022a036a93a9b55af2e71",
"34d2935a8c70f3a2b09212b354bc15a8",
"32ac92729760f800fef6108a8d25b64f",
#"6942f7896260b87edf70e183cc1975ce",#5
"54b7f665bce565e838572034e67ae743",
"027a5cdd181b3fb75fc990eb53a19571",
"4361a0e3885ab5e837b3d334b385847a",
#"0bdc508a17811a3a860d32749ad44e4b",#5
"b91caba63c053f299fce69f6c903d515",
"916586c8ac87cf1a18ea5d004facb87e",
#"afb175e63dfc6aacbbd5bfe1dca14fd7",#6
#"c28bb465d5de26aacb55c72e29910fb0",#5
"fb59891768280222f6270e1a260c3637",
"881bea88a78db4d68a474582c35bbac0",
#"f4fc7c7280f867525d5e93242e3db785",#5
#"44b33bf6be299625548c569e271bd2f3",#6
"424e7a32dd8a9d45aec0e5b9a0664de4",
"a7887cc809cf0d4df17fc5dafd03e4e7",
#"5a5f29d38303f9664ba1e1652b25fb72",#5
"1bf8fcb0a2dd77e48780712c559ab64f",
"5e58e27883fa86c163e7929fe27365ec",
#"94ed416723ce619a79d9bf5ecb292718",#5
#"05da33eab200f4c5b5ba3ed05beb2ec5",#p3 #5
"124bd1296bec0d9d93c7b52a71ad8d5b",
#"174d689df4b13b90121c3aaea1d015c4",#5
#"21ef05aed5af92469a50b35623d52101",#6
"29c3eea3f305d6b823f562ac4be35217",
#"3164552fada5eede958a988bbb215163",#5
#"34d9e14c87df4374163ba48265cd6729",#6
#"462fa40d604d2c9b642208f78c3ca84e",#6²
#"462fa40d604d2c9b642208f78c3ca84e",#6²
"4b70401e0604cc96e16d132408198e44",
#"611ba5ef155b93d1cc990c1e3dfebe03",#5
"63effa2530d088a06f071bc5f016f8d4",
#"64254db8396e404d9223914a0bd355d2",#5
#"675ff4d1cf0c143f6f8a83b5bf19af81",#6
#"6d76c1cb0ed1cbc1df98578e7b641743",#6
"6e67d70788fcb5b5befdf09a7ca39e64",
#"827ccb0eea8a706c4c34a16891f84e7b",#5
#"9174e5b543aa4e8fdc07cc9dae7b5c80",#6
#"adab360867b6bf1e2b57c050a2bc955f",#6
#"b750c583c4740415f8c803198ad9a318",#5
#"b7bc2a2f5bb6d521e64c8974c143e9a0",#5
#"c4ded2b85cc5be82fa1d2464eba9a7d3",#5
"cfc6678c720739386ff2506ac18debae",
"d4b35a0de71992ce8a5ba92571c6e679",
"db802e9da4df58a5c33c7ff033ccfd5a",
#"df4e169df0449eb32075ada85240d69b",#6
"e7a1897007ef65e67048383c6383d42c",
#"ecebb6d849809cf79fa2ba47c3730728",#5
#"f379eaf3c831b04de153469d1bec345e",#6
"fcea920f7412b5da7be0cf42b8c93759",
#"be92c9e5ed17e744987495eb902ae755",#p4 #5
#"d3860b43bbaa0d856594b2a408142b66",#6
"c1a31da84f15b59384b9ded1ba854559",
#"a81646a94cc6fa724b681864a5926b49",#5
#"416130d6a67c78075d1fefc3e071b465",#6
"a9d2084fe1f451fcc32812f2429fbe39",
#"79c0e0e60cdf6d263054b2b438605740",#5
"93587a352fa62a42818316a2efd0d24b",
"ec57009d3e7d7aed3c2ece4234109532",
#"f989faecc04ea881129a79b306e56780",#5
#"2f94ec8908eddf8008365131baa85199",#6
"b0746686b075bae7a527124bd29f00c0",
#"38621a4677e73b2af3b7d1ce4eb100b1",#5
#"5f40a47c3f947f901d892d6a090eee1a",#6
"b2c6425352fa75a8d21e90796f6ac500",
#"49a2a173892dc293ef6f5c809aa2f629",#5
#"ed8759baca899889fd37aabe74a70ee6",#6
"76debc3353fab98cc48c578c8151e1ba",
#"54eb39c3a0ab08f8e9c98146591274d4",#5
"d9773b85c256629d55fdecc7cf820d3d",
"2fc59c9049a3c1c48fc6d35ed71c3077",
#"c465278df113d710b4570ec350ad9f35",#5
#"fdd611a9a11fd4bfd57c7da89b4444d7",#6
"71a3a83fb3fcacfac95add398d423c9d",
#"75d7a0c380fbf4a9f52ba43640961c5c",#5
"a812210b2d037ca55406a71ca772e995",
"f78f82e104c0c379bb44d7ffc5056190",
#"dd5180fbc40449e73c422cb8a8f8f217",#5
"9f74ed31bc18825140ed548177931a53",
"78ee88aaf658c4859fc4e4cf3da5373f",
"0c258a93310361877683eb8fb0c17f38",#p5
#"0e549aa4a36ede9c67097e8f1072dafa",#5
#"15dd41acc5efaa8aea4a7d01cd69c523",#5
#"1a6b76d84300cb40797a630c797f8aaa",#5
"1d0eeedb7e2f414b38607b4fffbe6341",
#"1d18be116388d7d3fcd0ec0dd42b8d52",#5
"2297dbc46e3f3f240d7940ca890a7005",
"299ce6050351b04c931a660acf87d039",
"36d5b4898eb76bfad730cc1eca7fa9f9",
"37b956440e0048616664a640311c7a6f",
#"3899ee20e60b3ef9772978a349f46ca0",#5
"55b3044a3ba17dcd3ad438090468d267",
#"5a16f53859f8f1c9a601967c06631dd4",#5
"5c71e90c0491ee9a1799331c4a6411c6",
"6dd7db4d761e0cf724f354965ab18779",
#"7c3953e43f5be028902a8a02e074cf05",#5
"7d001a86ac707d9c12a47d1fe5166b3a",
#"8baecf4245dea00140772cf4f4c2a6c4",#5
"94884f9827a24fcdfa934792953f8b6b",
"96b3b4fbd1d872adb0b548b3539190d7",
"99336cda1cfbe1a7832161b6cc2c7b03",
"9b76acc4667d6ca9db858ff40463b56b",
"9ce46531f5dfe8e7e3a3b2b5a6f20011",
"a53c38ba9f01a10cf8b5135037f398ca",
"c08e84bd6985ffe136ad0c118bf6ee1e",
#"c3478c2094a898641265c99ca40b832d",#5
"e6fc2a230475c3c5aef2b1ad30aafe23",
"f6c08b3a8e00aff4f79566e02d105175",
"ff2293258ba258c071ce6cfb5fc0201e",
"ff39277e323556ac27a62c1f30565981"
] # lista com as hashes a serem quebradas

# criação da lista com os seguintes caracteres: [ a-z/A-Z ],[ 0-9 ],[ !@#$%&*()_-+=[]{}?/\|>< ]

alph0 = ["!","@","#","$","%","&","*","(",")","_","-","+","=","[","]","{","}","?","/","\\","|",">","<"]
alph0.extend(list(string.ascii_letters)) # extende a lista com as letras [ a-z/A-Z ]
alph0.extend(list(string.digits)) # extende a lista com os numeros [ 0-9 ]

alph1,alph2,alph3,alph4,alph5,alph6,alph7 = alph0,alph0,alph0,alph0,alph0,alph0,alph0 # cria listas de caracteres individualmente para cada posição da palavra

#alph1.reverse()
#alph2.reverse()
#alph3.reverse()
#alph4.reverse()
#alph5.reverse()
#alph6.reverse()
#alph7.reverse()

# teste para recuperar ultima posição da busca de palavras
try:
    last = open("./chave_final.txt","r") # le arquivo que armazena a ultima palavra testada
    last = last.readlines() # le as linhas do arquivo
    last = str(last[-1]) # armazena a ultima linha e transforma em string

    x0,y0,z0,a0,b0,c0,d0 = last[0],last[1],last[2],last[3],last[4],last[5],last[6] # separa cada letra da palavra em variaveis

    size = len(alph0) # tamanho total do dicionario de caracteres original

    # comentar neste ponto para paralelizar
    '''
    # corta a lista de caracteres inicial, da posição 1, para continuar de onde parou
    idx_list = [idx for idx, val in enumerate(alph0) if val == x0] # encontra a posição da ultima letra testada na lista de caracteres da PRIMEIRA letra da palavra

    dummy, alph1 = [alph1[i: j] for i, j in
            zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))] 
    '''
    ##############

    # comentar neste ponto para paralelizar o segundo caractere
    '''
    # corta a lista de caracteres inicial, da posição 1 (senhas de 7), para continuar de onde parou (considerando o uso de threads)
    idx_list = [idx for idx, val in enumerate(alph0) if val == x0] # encontra a posição da ultima letra testada na lista de caracteres da PRIMEIRA letra da palavra

    idx_list[0] = floor(idx_list[0]/cores) # 

    idx_list[0] = idx_list[0]*cores

    print(idx_list)

    dummy, alph1 = [alph1[i: j] for i, j in
            zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))] # separa a lista de caracteres original em duas, a partir do ultimo caractere testado

    # corta a lista de caracteres inicial, da posição 2, para continuar de onde parou
    idx_list = [idx for idx, val in enumerate(alph0) if val == y0] # encontra a posição da ultima letra testada na lista de caracteres da SEGUNDA letra da palavra

    dummy, alph2 = [alph2[i: j] for i, j in
            zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))] 
    '''
    ##############

    #comentar neste ponto para paralelizar o primeiro caractere

    # corta a lista de caracteres inicial, da posição 2 (senhas de 6), para continuar de onde parou (considerando o uso de threads)
    idx_list = [idx for idx, val in enumerate(alph0) if val == y0] # encontra a posição da ultima letra testada na lista de caracteres da SEGUNDA letra da palavra

    idx_list[0] = floor(idx_list[0]/cores)

    idx_list[0] = idx_list[0]*cores

    print(idx_list)

    dummy, alph2 = [alph2[i: j] for i, j in
            zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))] # separa a lista de caracteres original em duas, a partir do ultimo caractere testado

    ##################

    # corta a lista de caracteres inicial, das posiçoes 3 e 4, para continuar de onde parou
    idx_list = [idx for idx, val in enumerate(alph0) if val == z0]

    dummy, alph3 = [alph3[i: j] for i, j in
            zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))]             

    idx_list = [idx for idx, val in enumerate(alph0) if val == a0] 

    dummy, alph4 = [alph4[i: j] for i, j in
            zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))] 

except: # caso nao exista registro de ultima chave testada o script continua normalmente
    pass

# função que percorre o alfabeto e testa cada palavra

def percorre(y): # defina x para paralelizar o primeiro caractere e y para o segundo

    global alph1, alph2, alph3, alph4 # define os alfabetos como variaveis globais para recupera os valores originais

    #for x in alph1:
    #for y in alph2:
    for z in alph3:
        for a in alph4:
            for b in alph5:
                for c in alph6:
                    for d in alph7:
                        
                        teste5 = "%s%s%s%s%s"%(z,a,b,c,d) # primeira palavra (5 letras)
                        resultado5 = (hashlib.md5(teste5.encode())).hexdigest() # codifica a palavra para um hash md5 hexadecimal

                        # testa a palavra codificada com as hashes da lista
                        if resultado5 in hashlist:
                            out = open("./hashes.csv","a") # abre o aquivo das hashes para salvar
                            resultado = resultado5 + "," + teste5 + "\n" # cria variavel com chave e palavra decodificada
                            print(resultado) # printa a linha da chave e palavra
                            out.write(resultado) # salva a chave e a palavra no arquivo
                            out.close() # fecha o arquivo para salvar a chave instantaneamente
                        
                        teste6 = "%s%s%s%s%s%s"%(alph2[y],z,a,b,c,d) # segunda palavra (6 letras) com threads
                        #teste6 = "%s%s%s%s%s%s"%(y,z,a,b,c,d) # segunda palavra (6 letras)
                        resultado6 = (hashlib.md5(teste6.encode())).hexdigest()

                        if resultado6 in hashlist:
                            out = open("./hashes.csv","a")
                            resultado = resultado6 + "," + teste6 + "\n"
                            print(resultado)
                            out.write(resultado)
                            out.close()
                        
                        #teste7 = "%s%s%s%s%s%s%s"%(x,y,z,a,b,c,d) # terceira palavra (7 letras)
                        #teste7 = "%s%s%s%s%s%s%s"%(alph1[x],y,z,a,b,c,d) # terceira palavra (7 letras) com threads na primeira letra
                        teste7 = "!%s%s%s%s%s%s"%(alph2[y],z,a,b,c,d) # terceira palavra (7 letras)  com threads na segunda letra
                        resultado7 = (hashlib.md5(teste7.encode())).hexdigest()

                        if resultado7 in hashlist:
                            out = open("./hashes.csv","a") 
                            resultado = resultado7 + "," + teste7 + "\n"
                            print(resultado)
                            out.write(resultado)
                            out.close()

            estado = open("./chave_final.txt","w") # cria um arquivo para armazenar a ultima chave testada
            estado.write(teste7) # esvreve a ultima palavra no arquivo
            print(teste7) # printa a palavra de 7 letras para controle de progresso

            estado.close() # fecha o arquivo
        alph4 = alph0 # recupera as listas de caracteres completas
    alph3 = alph0
#alph2 = alph0


#percorre()
    
#t = Thread(target=percorre, args=())
#t.start()
    
# cria um processo para cada uma das hashes
#p1 = Process(target=percorre, args=())
# inicia o script rodando todas as hashes em paralelo
#p1.start()
#p1.join()

tam = len(alph0) # calcula tamanho da lista de caracteres

for x in range(0,tam,cores): # loop do tamanho do total de caracteres, iterando no numero de threads usado
    with multiprocessing.Pool(cores) as pool:

        # seleciona o numero de entradas na função
        if cores == 12:
            args = [x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8,x+9,x+10,x+11]
        elif cores == 9:
            args = [x,x+1,x+2,x+3,x+4,x+5,x+6,x+7,x+8]
        elif cores == 6:
            args = [x,x+1,x+2,x+3,x+4,x+5]
        results = pool.map(percorre, args)  
