x=1 
while [ $x -le 100 ]
do 

	if [ $(($x % 3 )) -eq 0 ] ;then
		echo "$x is divisible by 3"
	fi
        x=`expr $x + 1` 

done
