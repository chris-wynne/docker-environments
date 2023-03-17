# Docker Instructions

Below are instructions for setting up and using Docker.
### Docker Terraform Tool

1. Build docker file

```(bash)
docker build --rm -t tf-tool -f tf-tool.Dockerfile .
```

2. Run container in terminal

```(bash)
docker run --rm -it --mount type=bind,target=//root/code,source=/"$(pwd)" tf-tool
```

3. Exit container

```(bash)
exit
```

## Terraform Terminal Commands

These commands should be entered into the tf-tool Docker container terminal.

1. Navigate to the terraform folder

```(bash)
cd code/terraform-iac
```

2. Initialize terraform

```(bash)
terraform init
```

3. Plan terraform to spot issues before creating

```(bash)
terraform plan
```

4. Build

```(bash)
terraform apply
```

5. Destroy

```(bash)
terraform destroy
```
