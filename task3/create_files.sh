#!/usr/bin/env bash

HOSTNAME=$(hostname)
DATE_TIME=$(date +"%Y-%m-%d %H:%M:%S")

case $HOSTNAME in
  sftp1)
    NEIGHBORS=("192.168.56.12" "192.168.56.13")
    ;;
  sftp2)
    NEIGHBORS=("192.168.56.11" "192.168.56.13")
    ;;
  sftp3)
    NEIGHBORS=("192.168.56.11" "192.168.56.12")
    ;;
esac

for N in "${NEIGHBORS[@]}"; do
  FILENAME="created_by_${HOSTNAME}_at_$(date +'%Y%m%d_%H%M%S').txt"
  CONTENT="Created by: $HOSTNAME
DateTime: $DATE_TIME
"
  echo "$CONTENT" | ssh -o StrictHostKeyChecking=no -i /home/sftpuser/.ssh/id_rsa sftpuser@$N "cat > /home/sftpuser/$FILENAME"
done
