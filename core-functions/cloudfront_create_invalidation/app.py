import logging

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

cloudfront = boto3.client("cloudfront")
codepipeline = boto3.client("codepipeline")


def lambda_handler(event, context):
    try:
        distribution_id = event["CodePipeline.job"]["data"]["actionConfiguration"][
            "configuration"
        ]["UserParameters"]
        job_id = event["CodePipeline.job"]["id"]

        response = cloudfront.create_invalidation(
            DistributionId=distribution_id,
            InvalidationBatch={
                "Paths": {"Quantity": 1, "Items": ["/*"]},
                "CallerReference": job_id,
            },
        )
    except Exception as e:
        codepipeline.put_job_success_result(
            jobId=job_id, failureDetails={"type": "JobFailed", "message": str(e)}
        )
        return

    logger.info(response)
    codepipeline.put_job_success_result(jobId=job_id)
