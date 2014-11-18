rubygem-gem2rpm-srpm
====================

Wrapper for SRPM building tools for the gem2rpm rubygem.

This is pretty straightforward: I used 'gem install gem2rpm' to get
the gem2rpm tool, and then used it to build the RPM itself.

     gem2rpm --fetch > rubygem-gem2rpm.spec

It did not wind up detecting its own LICENSE, and the "templates"
files it uses were not set. It's also not working yet for RHEL 7
compilatoin which seems to lack the 'ruby(abi)' module for
dependencies and does odd things creating and needing "/usr/bin"
entries in its own build directory. But it's working well for RHEL 6
based operationg systems.

		Nico Kadel-Garcia <nkadel@gmail.com>
