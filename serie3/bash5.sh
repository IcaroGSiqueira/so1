# Construa um scrip que some o número 5 aos valores existentes em cada uma das linhas de um arquivo txt. Deverá ser gerado um outro arquivo com os valores decorrentes da soma. [subtrair, subtrair somente de valores superiores a 8, etc.]

echo "Nome do arquivo: "
read arq

for line in $(cat $arq)
do
	echo "$line + 5" | bc 

done > "novo_$arq"
