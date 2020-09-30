# Elabore um script utilizando uma estrutura de repetição for que imprima os dias da semana. [impressão condicional em função da data, considerando um mês inteiro]


for i in $(seq 1 30) ;
do
	for j in 1 2 3 4 5 6 7;
	do
		let $i++
		let $j++

		echo $j
done