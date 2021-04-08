#!/bin/bash

docker run -dit --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=pass -e MYSQL_DATABASE=my_db mysql

sleep 10

cat persons.sql | docker exec -i mysql mysql -u root -ppass my_db

