from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    App
    # aws_sqs as sqs,
)
from constructs import Construct

class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        #Vpc
        VpcProj = ec2.Vpc(self,'VpcProject',
                          vpc_name='Demo Vpc',
                          ip_addresses=ec2.IpAddresses.cidr('10.0.0.0/16'),nat_gateways=0)
        #Security Group
        SG=ec2.SecurityGroup(self,'SGProject',vpc=VpcProj,security_group_name ='allow http traffic',
                   allow_all_outbound =True)
        SG.add_egress_rule(ec2.Peer.any_ipv4(),ec2.Port.tcp(80),'allow http traffic')

        #Ec2 Instance
        EC2=ec2.Instance(self,'EC2InstanceforProject',vpc=VpcProj,
                         vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
                         security_group=SG,
                         instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2,ec2.InstanceSize.MICRO),
                        machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
                        key_name='demokeypair')
        user_data = self.read_file('./infra/userdata.sh')
        EC2.add_user_data(user_data)

    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf8') as file:
            return file.read()
        
app =App()
InfraStack(app, "VpcProjectStack")