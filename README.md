# demo-flask



#### Status Report

https://docs.google.com/document/d/1FH8R68dDC0DRArvTU1_IS1KUkcLb7MvPWTSeM5tA-Bg/edit#heading=h.zf568v8gwe4n

#### To Access the AWS MySQL db:

`mysql -h e6156-db.cm1wbnh1ss6q.us-east-2.rds.amazonaws.com -P 3306 -u admin -p` 

#### To Access the AWS EC2 instance:
`ssh -i "404NotFound-EC2-test-keypair.pem" ec2-user@ec2-3-142-189-48.us-east-2.compute.amazonaws.com`

#### EC2 Public IP addr:

`3.142.189.48`

#### Test Cases:

http://3.142.189.48:5000/imdb/artists/Gogh

http://3.142.189.48:5000/students/Zhejian%20Jin

......or any group numbers name 

#### How to run in EC2:

`python3 app.py`

