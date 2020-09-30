# Elabore um script utilizando uma estrutura de repetição for que imprima os dias da semana. [impressão condicional em função da data, considerando um mês inteiro]

for i in $(seq 1 30)
do
	date +"%A" --date="$i day"
done