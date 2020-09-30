# Elabore um script que incremente de 1 em 1 um valor impresso na tela, a partir de um primeiro parâmetro, até que seja atingido o valor do segundo parâmetro. Caso o segundo parâmetro seja menor ou igual que o primeiro a execução deve ser encerrada. [trabalhar com decremento ou o teste pode ser feito com a primeira linha de um arquivo, o qual será passado como parâmetro]

echo -n "Digite um Número: "
read i

echo -n "Digite o Número a ser atingido: "
read i2

echo "LISTA: "

if [ $i -gt $i2 ]
then
	break
fi

while [ $i -lt $i2 ]
do

	echo -n $i,
	echo -n " "
	echo $(($i * 3))

	let i--
done