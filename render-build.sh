#!/usr/bin/env bash
# This installs system dependencies required to build mysqlclient
apt-get update
apt-get install -y default-libmysqlclient-dev build-essential
