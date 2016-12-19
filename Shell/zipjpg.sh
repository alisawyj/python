#!/bin/bash
JPG=$(date -d +1day "+%Y%m%d")
curDate=$(date "+%Y%m%d")
SRC_DIR="/d/code_test"
function batch_convert() {
    for FILENAME in `ls $1`
    do
        if [ -d "$1/$FILENAME" ]
        then
            cd "$1/$FILENAME"
            batch_convert ./
        else
            if [ "${FILENAME##*.}" = "jpg" ];then
              NAME=${FILENAME##*/}
              NEW_FILE_NAME=${JPG}_${NAME}
              echo $FILENAME"---->"$NEW_FILE_NAME
              mv $FILENAME $NEW_FILE_NAME
            fi
        fi
    done
}


cd $SRC_DIR
if [ $? -ne 0 ];then
  echo "can not open target directory!"
  exit 2
fi

batch_convert ./
zip -r ${curDate}.zip ./*.jpg
