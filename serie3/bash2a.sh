#Desenvolva um script que pergunte por dois operandos e realize sobre os mesmos as quatro operações aritméticas.

while true ;
do

	echo -n "Digite o primeiro numero: "
	read n1

	echo -n "Digite o segundo numero: "
	read n2

	echo "Operação: "

	echo "Soma: "
	echo $(($n1 + $n2))

	echo "Subtração: "
	echo $(($n1 - $n2))

	echo "Multiplicação: "
	echo $(($n1 * $n2))

	echo "Divisão: "
 	echo $(($n1 / $n2))

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