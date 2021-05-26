from ..utils.check_all_extensions import check_all_extensions
from fractions import Fraction

print(check_all_extensions("", alphabet={"a","b", "c"}, rt=Fraction(7,4)))