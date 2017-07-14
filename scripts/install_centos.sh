#!/usr/bin/env bash
# Add Extra Packages for Enterprise Linux
#sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

# Install System Packages
sudo yum install -y $(grep -vE "^\s*#" packages-centos.txt | tr "\n" " ")


pip install -r requirements.txt