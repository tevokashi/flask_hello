

[![Build Status](https://dev.azure.com/stevan0539/test/_apis/build/status/build%20and%20push?branchName=master)](https://dev.azure.com/stevan0539/test/_build/latest?definitionId=1&branchName=master)
    
# flask_hello

To run this image use:

```docker container run -p 5000:5000/tcp -e SQLALCHEMY_DATABASE_URI='[database_connection_string]' -e REDISTOGO_URL='[redis_connection_string]' -d tevokashi/flask_hello```


To enqueue a job use 
 http://127.0.0.1:5000/api/v1/enqueue?val1=[number]&val2=[number]&tipo=[number]

For tipo uses:
0 = sum
1 = subtraction