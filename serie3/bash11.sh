# Desenvolva um script que teste o dia corrente da semana, caso seja sexta-feira, deverá ser impresso “SSSS”, caso contrário deverá ser impresso o dia corrente da semana

if [ "$(date '+%A')" = "sexta" ]
    then
        echo "SSSS"
else 
	echo "Dia da semana: $(date '+%A')"
fi