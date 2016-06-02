#!/bin/bash
file="file.txt"
if [ -s $file ]
then
	count='tail -1 file.txt | cut -d ":" -f1'
	count=$(($count+1))
else
	count="1"
fi
while true
do
	clear
	echo "[0].Exit"
	echo "[1].Add a people information"
	echo "[2].search a people information"
	echo "[3].modify a people information"
	echo "[4].delete a people information"
	echo -n "your choice(0,1,2,3 or 4):"
	read key 
	case $key in 
	0) exit;;
	1) clear
	echo "[${count}]:"
	read -p "Enter your name:" name
	read -p "Enter your phone number:" phone
	read -p "Enter your sex:" sex
	read -p "Enter your age:" age
	echo "$count:$name:$phone:$sex:$age" >> file.txt
	count=$(($count+1))
	;;
	2) clear
	read -p "Input a keyword:" word
	clear
	grep $word $file
	read -p "Press enter to continue...." Enter
	;;
	3) clear
	read -p "Input modify keyword information:" word
	read -p "Input new word:" nword
	sed -i "s/"$word"/"$nword"/g" $file
	;;
	4) clear
	read -p "Input delete poeple's name:" name
	sed -i '/'$name'/d' $file
	read -p "Press enter to continue...." Enter
	;;
	esac
done	
	
	
	

