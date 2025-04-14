from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI

with scanner.find_toy(timeout=45) as toy:
    with SpheroEduAPI(toy) as api:
        api.spin(360, 1)