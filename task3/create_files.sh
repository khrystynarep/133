#!/usr/bin/env bash

HOSTNAME=$(hostname)
DATE_TIME=$(date +"%Y-%m-%d %H:%M:%S")

case $HOSTNAME in
  sftp1) NEIGHBORS=("192.168.56.12" "192.168.56.13") ;;
  sftp2) NEIGHBORS=("192.168.56.11" "192.168.56.13") ;;
  sftp3) NEIGHBORS=("192.168.56.11" "192.168.56.12") ;;
esac

for N in "${NEIGHBORS[@]}"; do
  TARGET_HOST=$(ssh -i /home/sftpuser/.ssh/id_rsa -o StrictHostKeyChecking=no sftpuser@$N "hostname")
  LOG_ENTRY="$DATE_TIME | Created connection from $HOSTNAME to $TARGET_HOST"

  echo "$LOG_ENTRY" | ssh -i /home/sftpuser/.ssh/id_rsa -o StrictHostKeyChecking=no sftpuser@$N \
    "echo \"$LOG_ENTRY\" >> /home/sftpuser/connection_log.txt"
done
