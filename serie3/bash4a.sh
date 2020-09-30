# Construa um scrip que some os valores colocados em um arquivo do tipo TXT. Deve ser colocado um valor por linha no arquivo. O nome do arquivo deverá ser passado como parâmetro. [variante: multiplicar (dividir, somar, etc.) as linhas do arquivo por uma constante passada como parâmetro, e gerar um novo arquivo]

echo "Nome do arquivo: "
read arq

echo "Digite o operador(+,-,*,/): "
read op

echo "Digite o numero : "
read n

for line in $(cat $arq)
do
	echo "$line $op $n" | bc 

done > "novo_$arq"
