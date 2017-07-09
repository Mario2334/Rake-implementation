
from RAKE import Rake

text = '''
Anyone know a reasonable circuit for programming PALs?  I am interested
in programming a wide range of EPLDs but would be happy with something 
that could handle a 22V10 or thereabouts.

Thanks in advance,
--Tim
'''


print(Rake('Stop_list.txt').run(text))