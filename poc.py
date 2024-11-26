from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import APIGateway, Route53
from diagrams.aws.management import SSM, Cloudwatch

with Diagram("PoC architecture", show=False):
    dns = Route53("Route 53")
    api_gateway = APIGateway("API Gateway")
    lambda_func = Lambda("Lambda")
    rds = RDS("RDS Aurora Serverless v2")
    parameter_store = SSM("Parameter Store")
    cloudwatch = Cloudwatch("CloudWatch Logs and Metrics")

    dns >> api_gateway >> lambda_func
    lambda_func >> rds
    rds >> parameter_store
    lambda_func >> cloudwatch
