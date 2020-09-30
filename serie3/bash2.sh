#Desenvolva um script que pergunte por dois operandos e a operação a ser realizada. Devem ser permitidas no mínimos as quatro operações aritméticas básicas (+, -, x e /). Os operandos devem ser perguntados na tela, bem como a operação a ser efetuada. Ao final de cada operação, deverá ser feita a pergunta: Realizar nova operação? [variar o número de operandos e operações]

while true ;
do

	echo -n "Digite um Operador (+, -, x e /): "
	read i

	echo -n "Digite o primeiro numero: "
	read n1

	echo -n "Digite o segundo numero: "
	read n2

	echo "Operação: "

	if [ $i = "+" ]
	then
		echo "Soma: "
		echo $(($n1 + $n2))

	elif [ $i = "-" ]
	then
		echo "Subtração: "
		echo $(($n1 - $n2))

	elif [ $i = "x" ]
	then
		echo "Multiplicação: "
	 	echo $(($n1 * $n2))

	elif [ $i = "/" ]
	then
		echo "Divisão: "
	 	echo $(($n1 / $n2))
	fi

	echo "Realizar nova operação? s/n "
	read rt

	if [ $rt = "s" ]
	then
		echo " Nova Operação "
	else
		echo " Fim da Operação "
		break;
	fi
done