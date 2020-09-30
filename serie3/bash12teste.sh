#Crie um script que imprima o dia da semana. Associe 1 ao domingo, e imprima os dias faltantes até sábado.
if [ "$(date '+%A')" = "quarta" ]
    then
       for i in $(seq 1 4)
do
	echo -n $i,
	echo -n " "
	date +"%A" --date="quarta $i day" 
done
fi