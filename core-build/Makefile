STACK_NAME=core-build

AWS_PROFILE=default
AWS_REGION=us-east-1

GITHUB_TOKEN=dummy

all: template.yaml
	aws cloudformation deploy \
		--profile=$(AWS_PROFILE) \
		--region=$(AWS_REGION) \
		--capabilities=CAPABILITY_IAM \
		--no-fail-on-empty-changeset \
		--stack-name=$(STACK_NAME) \
		--template-file=$< \
		--parameter-overrides \
			GithubToken=${GITHUB_TOKEN}
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
