#将jpg格式的图片改一下命名且打包成zip格式
JPG=$(date -d +1day "+%Y%m%d")
curDate=$(date "+%Y%m%d")
SRC_DIR="../picture"

if [ -z $JPG ];then
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
		NAME=${FILENAME##*/}
		NEW_FILE_NAME=${JPG}_${NAME}
    fi
	echo $FILENAME"---->"$NEW_FILE_NAME
	mv $FILENAME $NEW_FILE_NAME
done
zip -r ${curDate}.zip ./*.jpg