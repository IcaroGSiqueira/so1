# Construa um script que receba como parâmetro dois operandos e a operação aritmética a ser realizada. Faça previsão para suportar as quatro operações (+, -, x e /).

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