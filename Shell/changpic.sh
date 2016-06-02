#将不同类型的图片分类重命名
PNG="png_"
JPG="jpg_"
SRC_DIR="../picture"
SUFFIXPNG=".PNG"
SUFFIXJPG=".JPG"

if [ -z $PNG ] || [ -z $JPG ];then
        echo "one parameter is missing!"
	exit 1
fi

cd $SRC_DIR
if [! $? -eq 0];then
      echo "can not open target directory!"
      exit 2
fi

FILE_LIST=`ls ./`
for FILENAME in $FILE_LIST ;do
	if [ "${FILENAME##*.}" = "JPG" ];then
		COUNT=$(( $COUNT + 1 ))
		NEW_FILE_NAME=$JPG$COUNT$SUFFIXJPG
	elif [ "${FILENAME##*.}" = "PNG" ];then
		i=$(($i+1))
		NEW_FILE_NAME=$PNG$i$SUFFIXPNG
    fi
	echo $FILENAME"---->"$NEW_FILE_NAME
	mv $FILENAME $NEW_FILE_NAME
done



