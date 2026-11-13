import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"arches_exmoor"), "arches_exmoor.urls", name="arches_exmoor"),
)
