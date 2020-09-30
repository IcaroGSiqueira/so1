# Crie um script que imprima o dia da semana. Associe 1 ao domingo, e imprima os dias faltantes até sábado. [imprimir os dias do mês corrente que irão cair em uma quarta-feira]

for i in $(seq 1 7)
do
	dia=$(date +"%A" --date="$saturday $i day")
	if [ "$(date '+%A' --date="today")" ]
	then
		echo -n $i,
		echo -n " "
		echo $dia
	fi
done