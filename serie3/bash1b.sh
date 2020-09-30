#Crie um script que liste na tela números decrescentes e ao lado a sua multiplicação por 3. Os números deverão decrescer de 1 em 1 até zero, a partir de um valor inicial passado como parâmetro quando script é chamado.

echo -n "Digite um Número: "
read i
echo "LISTA: "
while [ $i -gt 0 ]
do

	echo -n $i,
	echo -n " "
	echo $(($i * 3))

	let i--
done