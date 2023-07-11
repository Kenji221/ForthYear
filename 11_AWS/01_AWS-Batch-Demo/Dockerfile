FROM amazonlinux:2
RUN yum -y install which unzip python3 pip3
RUN pip3 install boto3
ADD importUser.py /usr/local/bin/importUser.py
WORKDIR /tmp
USER nobody
ENTRYPOINT ["/usr/local/bin/importUser.py"]