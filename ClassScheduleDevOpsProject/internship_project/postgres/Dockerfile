FROM postgres:15

ENV POSTGRES_DB=class_schedule
ENV POSTGRES_USER=your_user
ENV POSTGRES_PASSWORD=your_password

COPY class_schedule.dump /docker-entrypoint-initdb.d/class_schedule.dump
COPY init.sh /docker-entrypoint-initdb.d/init.sh

RUN chmod +x /docker-entrypoint-initdb.d/init.sh
