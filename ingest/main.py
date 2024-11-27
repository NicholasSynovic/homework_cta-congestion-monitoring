import json

import cta
import cta.directors
import cta.directors.alert

d = cta.directors.alert.AlertAPIDirector()

resp = d.getRouteStatus(type=["station"])

json.dump(obj=resp.json(), fp=open("test2.json", "w"), indent=4)
