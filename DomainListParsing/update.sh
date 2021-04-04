#!/bin/bash

cd /var/baddomains
rm /var/baddomains/domains.list
rm /var/baddomains/hosts
rm /var/baddomains/BadDomains.txt
python3 /var/baddomains/Parse.py
cp /var/baddomains/BadDomains.txt /etc/squid/
