# Crie um script que liste na tela 10 números crescentes (de 1 em 1) a partir de um valor inicial fornecido quando script é chamado (passado como parâmetro) [variar o total de números, o fator de crescimento e o critério de parada].

echo -n "Digite um Número: "
read i
cont=0 
echo "LISTA: "
while [ $cont -lt 10 ] # total de numeros, -lt = menor que -gt = maior que
do
	let cont=cont+1 # fator de crescimento

	echo $i

	let i++
done