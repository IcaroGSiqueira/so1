# Construa um script que receba como parâmetro dois operandos e a operação aritmética a ser realizada. Faça previsão para suportar as quatro operações (+, -, x e /). Os operandos e o resultado deverão ser impressos na tela ao final.



echo -n "Digite um Operador (+, -, x e /): "
read i

echo -n "Digite o primeiro numero: "
read n1

echo -n "Digite o segundo numero: "
read n2

echo 
echo "Operação: "

echo -n "Operando 1: "
echo $n1

echo -n "Operando 2: "
echo $n2

if [ $i = "+" ]
then
	echo -n "Soma: "
	echo $(($n1 + $n2))

elif [ $i = "-" ]
then
	echo -n "Subtração: "
	echo $(($n1 - $n2))

elif [ $i = "x" ]
then
	echo -n "Multiplicação: "
 	echo $(($n1 * $n2))

elif [ $i = "/" ]
then
	echo -n "Divisão: "
 	echo $(($n1 / $n2))
fi
