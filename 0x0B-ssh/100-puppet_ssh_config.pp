#!/usr/bin/env bash
# For using puppet code to effect and add changes to config file

file { 'ect/ssh/ssh_config':
	ensure => present

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	"
}
