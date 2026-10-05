import sys
sys.path.insert(0, "../lib")
## Importo la posizione della libreria schema perché non la trova più in automatico... capire perché!
#sys.path.append(r"./Python311/Lib")
sys.path.append(r"C:\Program Files (x86)\SmartBear\TestComplete 15\Bin\Extensions\Python\Python311\Lib")

from schema import Schema, Or, Optional


"""
  Schema atteso gli interfaccia GET /v1/riskaudit/{abi}/templates/{template}/note (TC0001)
  response body: TemplateDTO
"""
TemplateDTO = Schema(
  {
    "id": str,
    "note": Or(str, None)
  }
)


"""
  Schema atteso gli interfaccia PUT /v1/riskaudit/{abi}/templates/{template}/note (TC0002)
  response body: GenericResponse
"""
GenericResponse = Schema(
  {
    "id": int
  }
)


"""
  Schema atteso gli interfaccia POST /v1/riskaudit/{abi}/templates/templateC/traded-instruments/search (TC0004)
  response body: ListResultTemplateCTradedInstrumentsSearchDTO
"""
ListResultTemplateCTradedInstrumentsSearchDTO = Schema(
  {
    "data": [
      {
        "operationDate": str,
        "isin": str,
        "security": str,
        "direction": str,
        "amountEuros": str,
        "intermediary": str
      }
    ],
    "total": int
  }
)


"""
  Schema atteso gli interfaccia POST /v1/riskaudit/{abi}/templates/templateC/held-instruments/search(TC0005)
  response body: ListResultTemplateCHeldInstrumentsSearchDTO
"""
ListResultTemplateCHeldInstrumentsSearchDTO = Schema(
  {
    "data": [
      {
        "balanceDate": str,
        "isin": str,
        "security": str,
        "amountEuros": Or(int, float),
        "depositary": str
      }
    ],
    "total": int
  }
)


"""
  Schema atteso gli interfaccia POST /v1/riskaudit/{abi}/templates/templateB/search (TC0006)
  response body: ListResultTemplateBSearchDTO
"""
ListResultTemplateBSearchDTO = Schema(
  {
    "data": [
      {
        "limit": str,
        "issuer": Or(None, str),
        "waiver": str,
        "thresholdCrossingDate": str,
        "returnDate": Or(None, str),
        "thresholdValue": Or(int, float),
        "maxValue": Or(int, float),
        "avgValue": Or(int, float),
        "endPeriodValue": Or(int, float),
        "thresholdCrossingDays": Or(int, float)
      }
    ],
    "total": int
  }
)


"""
  Schema atteso gli interfaccia POST /v1/riskaudit/{abi}/templates/templateA/search (TC0007)
  response body: ListResultTemplateASearchDTO
"""
ListResultTemplateASearchDTO = Schema(
  {
    "data": [
      {
        "id": int,
        "date": str,
        "isin": str,
        "description": str,
        "nozionale": str,
        "ptf_htc": Or(int, float),
        "aCase": str,
        "frequency": {
          "limit": int,
          "value": int
        },
        "significance": {
          "limit": int,
          "value": int
        },
        "sell_percentage": Or(int, float)
      }
    ],
    "total": int
  }
)