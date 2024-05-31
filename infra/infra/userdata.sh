sudo su
yum  update -y
yum install -y httpd

systemct1 start httpd
systemct1 enable httpd

echo "<h1> Hello from AWS CDK Project with  Ritik </h1>" > /var/www/html/index.html
