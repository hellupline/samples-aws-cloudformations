STACK_NAME=core-functions

AWS_PROFILE=default
AWS_REGION=us-east-1

ARTIFACT_STORE_BUCKET_NAME=$$(aws cloudformation describe-stacks \
	 --profile=$(AWS_PROFILE) \
	 --region=$(AWS_REGION) \
	 --stack-name=core-build \
	 --query="Stacks[].Outputs[?OutputKey == 'ArtifactStoreBucket'].OutputValue" \
	 --output text)


all: packaged.yaml
	aws cloudformation deploy \
		--profile=$(AWS_PROFILE) \
		--region=$(AWS_REGION) \
		--capabilities=CAPABILITY_IAM \
		--no-fail-on-empty-changeset \
		--stack-name=$(STACK_NAME) \
		--template-file=$<
	@aws cloudformation describe-stack-resources \
		--profile=$(AWS_PROFILE) \
		--region=$(AWS_REGION) \
		--stack-name=$(STACK_NAME) \
		--query='StackResources[].{LogicalResourceId: LogicalResourceId, PhysicalResourceId: PhysicalResourceId, ResourceStatus: ResourceStatus}' \
		--output=table
	@aws cloudformation describe-stacks \
		--profile=$(AWS_PROFILE) \
		--region=$(AWS_REGION) \
		--stack-name=$(STACK_NAME) \
		--query="Stacks[].Outputs[].{OutputKey: OutputKey, Description: Description, OutputValue: OutputValue}" \
		--output table


packaged.yaml: template.yaml cloudfront_create_invalidation/app.py
	aws cloudformation package \
		--profile=$(AWS_PROFILE) \
		--region=$(AWS_REGION) \
		--s3-bucket=$(ARTIFACT_STORE_BUCKET_NAME) \
		--s3-prefix=cf-packages \
		--template-file=$< \
		--output-template-file=$@
