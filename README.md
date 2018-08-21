# AWS Lambda pymssql

AWS Lambda pymssql proof of concept with RDS MSSQL access based in `lambci/lambda:build-python3.6` docker image for easy testing and deployment.

##Before you start
Manually edit the credentials in the `lambda_function.py` file.
This is a PoC only, it is recommended to **set these in your environment** and not hardcode them in the file.

Create a table called `test` with ID and Name fields and insert some dummy data or adapt the query `cursor.execute('SELECT * FROM test')` to fit your needs.


##Setup
After installing docker, download the python3.6 lambda build using:
`docker pull lambci/lambda:build-python3.6`

Navigate to this repository and mount it on the container with:
`docker run -v "$PWD":/var/task -it lambci/lambda:build-python3.6 bash`

Once inside the container create a virtual environment and activate it with:

```
virtualenv aws
. ./aws/bin/activate
```

Install the needed dependencies with:

```
yum install -y freetds-devel
pip install -r requirements.txt
cp /usr/lib64/libsybdb.so aws/lib/python3.6/site-packages/
```

<br>
**You're now ready to run the example code with:**

`python lambda_function.py`


##Deployment

When you're ready to deploy your code to Lambda, use the following to create a zip with all the needed libraries from your environment with:

```
cd lambda/lib/python3.6/site-packages
zip -r ../../../../lambda_deploy.zip *
cd ../../../lib64/python3.6/site-packages
zip -r ../../../../lambda_deploy.zip *
exit
```

Finally add your code to the package with:
```
zip lambda_deploy.zip lambda_function.py
```


##Adding more packages
Simply add the package names to `requirements.txt` and import them in the `lambda_function.py`. You should be good to go