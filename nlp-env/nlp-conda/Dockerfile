# Start with Ubuntu 20.04
FROM ubuntu:20.04

# Set the working directory
WORKDIR /app

# Disable prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Update package index and upgrade packages
RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y wget bzip2 ca-certificates curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#add SSL certs (remove this if not an ARUP user)
#---------------------------------------------------------
COPY ./build/*.crt /usr/local/share/ca-certificates/
RUN update-ca-certificates
#---------------------------------------------------------

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -t -i -p -y
ENV PATH="/opt/conda/bin:${PATH}"

# Set SSL for Conda (remove this if not an ARUP user)
#---------------------------------------------------------
RUN conda config --set ssl_verify "/usr/local/share/ca-certificates/curl-ca-bundle.crt"

#This is an SSL workaround
# ENV CONDA_SSL_VERIFY=false
#---------------------------------------------------------

COPY environment_nlp.yml /
RUN conda env create -f /environment_nlp.yml && conda clean -a 

# Activate the environment
RUN echo "source activate arup_nlp_prog" >~/.bashrc
ENV PATH /opt/conda/envs/arup_nlp_prog/bin:$PATH

# The code below is to download specific nlkt data not
# RUN python -m nltk.downloader punkt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT [ "python3" ]
