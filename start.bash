docker-compose stop
docker-compose rm
rm -r data/
docker-compose up -d --build
sleep 1m
bash restore_db.bash
docker-compose restart
