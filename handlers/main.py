#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def post(self):
        kilometros = str(self.request.get("edKm", "0"))
        tiempo = str(self.request.get("edTm", "0"))
        consumo_medio = str(self.request.get("edCm", "0"))

        if len(kilometros.strip()) == 0:
            kilometros = -1
        if len(tiempo.strip()) == 0:
            tiempo = -1
        if len(consumo_medio.strip()) == 0:
            consumo_medio = -1

        if kilometros != -1 and tiempo != -1 and consumo_medio != -1 and kilometros.isdigit() and tiempo.isdigit() and consumo_medio.isdigit() and float(tiempo) != 0:
            velocidad_media = float(kilometros)/float(tiempo)
            consumo_total = float(consumo_medio)*float(kilometros)
            self.response.write("Velocidad media: " + str(velocidad_media) + " Km/h y el consumo total: " + str(consumo_total) + " L")
        else:
            self.response.write("Los datos introducidos no son correctos.")


app = webapp2.WSGIApplication([
    ('/hello', MainHandler)
], debug=True)
