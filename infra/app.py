#!/usr/bin/env python3
import os

from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    App
    # aws_sqs as sqs,
)

from infra.infra_stack import InfraStack


app = App()
InfraStack(app, "VpcProjectStack",
   )

app.synth()
