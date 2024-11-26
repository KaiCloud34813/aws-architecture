from diagrams import Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import ALB, Route53
from diagrams.aws.management import SSM, Cloudwatch
from diagrams.aws.security import Cognito


with Diagram("Optimized poc", show=False):
    dns = Route53("Route 53")
    alb = ALB("Application Load Balancer")
    ecs = ECS("ECS Fargate")
    rds = RDS("RDS Aurora Serverless v2")
    cognito = Cognito("Cognito Authentication")
    parameter_store = SSM("Parameter Store")
    cloudwatch = Cloudwatch("CloudWatch Logs and Metrics")

    dns >> alb >> ecs
    ecs >> rds
    ecs >> parameter_store
    ecs >> cloudwatch
    alb >> cognito 
