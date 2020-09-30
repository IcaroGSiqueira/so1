# Construa um script utilizando um laço While que informe na tela se o arquivo “pagamentos.txt” existe. Caso o arquivo exista deve ser impresso “arquivo existe”, caso contrário “arquivo não existe”. O script deve permanecer em excução, e o arquivo deve ser criado/apagado através de outro terminal. [verificar se o conteúdo da primeira linha é maior que N, e realizar algo - pode ser a soma das três primeiras linhas ser maior que N, e então fazer algo]

echo -n "Digite um numero: "
read num

echo -n "Nome do arquivo: "
#read arq
arq="pagamentos.txt"

echo $arq
echo

while true
do
	if [ "$(find . -name pagamentos.txt)" ]
	then
		echo "arquivo existe"
		if [ "$(head -n 1 $arq)" -gt $num ]
		then
			echo "primeira linha maior que $num"
		fi
	else
		echo "arquivo não existe"
	fi
	sleep 2

done