# For more information, please refer to https://aka.ms/vscode-docker-python
FROM continuumio/miniconda3:4.12.0

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /root

# Install pip requirements
COPY requirements.txt /root/
RUN conda update -y conda 
RUN conda install -y --file /root/requirements.txt -c conda-forge -c anaconda

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT [ "python3" ]
