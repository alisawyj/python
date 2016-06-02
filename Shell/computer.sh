read -p "input a number:" num1
read -p "input a number:" num2
read -p "unput a operator:" oprt

case $oprt in
+) let "result=num1+num2"
echo $result;;
-) let "result=num1-num2"
echo $result;;
/) awk 'BEGIN{printf"%.2f\n",'$num1'/'$num2'}';;
*) let "result=num1 * num2"
echo $result;;
esac