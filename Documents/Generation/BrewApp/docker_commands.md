## Docker Terminal Commands

docker run --rm -it debian

docker run -it -v $(pwd)/source:/path/to/app debian
cd path/to/app
ls

root@9003c5778d9d:/# exit

docker ps
docker ps -a


docker kill <container_name>
docker stop <container_name>



docker run -v $(pwd)/init.sql:/docker-entrypoint-initdb.d/init.sql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password123 mysql