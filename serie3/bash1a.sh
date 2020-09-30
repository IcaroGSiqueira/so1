# Crie um script que liste na tela 10 números crescentes e ao lado o seu quadrado. Os números deverão crescer de 1 em 1, a partir de um valor inicial passado como parâmetro quando script é chamado.

echo -n "Digite um Número: "
read i
cont=0
echo "LISTA: "
while [ $cont -lt 10 ]
do
	let cont=cont+1
	
	echo -n $i,
	echo -n " "
	echo $(($i ** 2))
	#echo "sqrt($i)"|bc

	let i++
done