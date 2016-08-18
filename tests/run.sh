#! /bin/bash

docker build -t centos7-systemd centos/7/
docker run --detach --privileged --name RHEL7-CIS -v $(pwd)/..:/ansible -v /sys/fs/cgroup:/sys/fs/cgroup centos7-systemd
docker exec -i -t RHEL7-CIS ansible-playbook -i "localhost," -c local /ansible/tests/test.yml
