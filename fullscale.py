from diagrams import Diagram
from diagrams.aws.compute import EKS
from diagrams.aws.database import RDS
from diagrams.aws.network import ALB, Route53, CloudFront, APIGateway
from diagrams.aws.security import Cognito
from diagrams.aws.management import Cloudwatch
from diagrams.aws.analytics import Athena
from diagrams.aws.storage import S3
from diagrams.aws.devtools import Codepipeline, Codebuild, Codedeploy, XRay

with Diagram("Full-Scale", show=False):
    dns = Route53("Route 53")
    cloudfront = CloudFront("CloudFront CDN")
    api_gateway = APIGateway("API Gateway")
    alb = ALB("Application Load Balancer")
    eks_cluster = EKS("EKS Cluster")
    aurora = RDS("Aurora Global Database")
    cognito = Cognito("Cognito Authentication")
    cloudwatch = Cloudwatch("CloudWatch Logs and Metrics")
    xray = XRay("X-Ray Distributed Tracing")
    s3 = S3("S3 Logs Storage")
    athena = Athena("Athena Query Analytics")
    pipeline = Codepipeline("CodePipeline")
    build = Codebuild("CodeBuild")
    deploy = Codedeploy("CodeDeploy")


    dns >> cloudfront >> api_gateway >> alb
    api_gateway >> cognito
    alb >> eks_cluster
    eks_cluster >> aurora
    eks_cluster >> cloudwatch
    eks_cluster >> xray
    cloudfront >> s3
    s3 >> athena
    pipeline >> build >> deploy >> eks_cluster
