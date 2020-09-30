# Elabore um script utilizando uma estrutura de repetição for que imprima os dias da semana e ao lado o número correspondente (associe o domingo ao número 1).

for i in $(seq 1 30)
do
	echo -n $i,
	echo -n " "
	date +"%A" --date="Saturday $i day" 
done