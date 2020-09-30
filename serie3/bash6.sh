# Elabore um script que identifique qual linha tem o maior valor em um arquivo TXT. Cada linha do arquivo terá apenas um número e o maior valor deverá ser impresso na tela. [qual linha tem o menor valor, quais linhas tem números pares]

echo "Nome do arquivo: "
read arq

linemai=$(head -n 1 $arq)

for line in $(cat $arq)
do
	if [ $line -gt $linemai ]
	then
		linemai=$line
	fi
done
echo $linemai