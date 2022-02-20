# Curso Propedéutico de Python para Launch X - Innovacción Virtual.
# Explorer: Daniel Campos (https://www.github.com/giusniyyel)

from datetime import *
from dateutil.relativedelta import *

now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)