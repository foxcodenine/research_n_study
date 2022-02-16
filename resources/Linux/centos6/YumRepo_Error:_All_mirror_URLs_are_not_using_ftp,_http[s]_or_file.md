Centos 6 version met its EOL last month (November 30, 2020)

You can use one of the unofficial mirrors listed by centos in your /etc/yum.repos.d/CentOS-Base.repo. In my case (6.10) I used the mirror http://mirror.nsc.liu.se/centos-store/6.10/ and it worked smoothly:

	[base]
	name=CentOS-$releasever - Base
	baseurl=http://mirror.nsc.liu.se/centos-store/6.10/os/$basearch/
	gpgcheck=1
	gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
	# same for the others [updates] etc in the file


A copy of this /etc/yum.repos.d/CentOS-Base.repo file has been copy to this directory for reference.

Solution found at: https://stackoverflow.com/questions/21396508/yumrepo-error-all-mirror-urls-are-not-using-ftp-https-or-file
