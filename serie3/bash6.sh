# Elabore um script que identifique qual linha tem o maior valor em um arquivo TXT. Cada linha do arquivo terá apenas um número e o maior valor deverá ser impresso na tela. [qual linha tem o menor valor, quais linhas tem números pares]

echo "Nome do arquivo: "
read arq

for line in $(cat $arq)
do
	if [ $line -gt 8 ]
	then
		echo "$line - 5" | bc
	fi
done > "novo_$arq"
