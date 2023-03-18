echo Restore Userend
cat Userend/db_userend.sql | docker exec -i dbuserend psql -U postgres

echo Restore Frontend
cat Frontend/db_frontend.sql | docker exec -i dbfrontend psql -U postgres

echo Restore Backend
cat Backend/db_backend.sql | docker exec -i dbbackend psql -U postgres
