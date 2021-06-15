from ..utils.critical_exponent import critical_exponent
from ..utils.morphism import Morphism

dejeans_morphism=Morphism({
    "0": "0120212012102120210",
    "1": "1201020120210201021",
    "2": "2012101201021012102"
})

words=[dejeans_morphism.calculate(word) for word in ["010","012","020","021" ]]

for word in words:
    print(critical_exponent(word))