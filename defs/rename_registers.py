import re

filename = "STM32F10X_CL.xml"
curr_group = None
curr_reggroup = None

with open(filename) as f:
  for line in f:
    m_group = re.search(r'\bgroup\b\s\bname\b="(\w+)"',line)
    m_reggroup = re.search(r'\bregistergroup\b\s\bname\b="(\w+)"',line)
    m_reg = re.search(r'\bregister\b\s\bname\b="(\w+)"',line)
    if m_group:
#print "Matched group name:", m_group.group(1)
      curr_group = m_group.group(1)
#      print "Curr_group: ",curr_group
    elif m_reggroup:
#print "Matched registergroup name:", m_reggroup.group(1)
      curr_reggroup = m_reggroup.group(1)
#      print "Curr_reggroup: ",curr_reggroup

    if m_reg:
#print "Matched register name:", m_reg.group(1)
      line_new = line.replace(curr_group,curr_reggroup)
      print line_new,
    else:
      print line,
