#!/usr/bin/env bash
# For using puppet code to effect and add changes to config file

file { 'etc/ssh/ssh_config':
	ensure => present

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	"
}
