import sys
sys.path.insert(0, "../lib")
## Importo la posizione della libreria schema perché non la trova più in automatico... capire perché!
#sys.path.append(r"./Python311/Lib")
sys.path.append(r"C:\Program Files (x86)\SmartBear\TestComplete 15\Bin\Extensions\Python\Python311\Lib")

from schema import Schema, Or, Optional


"""
  Schema atteso gli interfaccia POST /v1/riskaudit/waiver/waiver/search (TC0028)
  response body: ListResultWaiverSearchDTO
"""
ListResultWaiverSearchDTO = Schema(
  {
    "data": [
      {
        "date": str,
        "legalEntity": {
          "abi": str,
          "name": str
        },
        "threshold": str,
        "waiver": str,
        "emailSentDate": Or(None, str),
        "note": Or(None, str),
        "creationDate": str
      }
    ],
    "total": int
  }
)


"""
  Schema atteso gli interfaccia POST /v1/riskaudit/waiver/target/search (TC0029)
  response body: ListResultTargetSearchDTO
"""
ListResultTargetSearchDTO = Schema(
  {
    "data": [
      {
        "date": str,
        "legalEntity": {
          "abi": str,
          "name": str
        },
        "strategicTarget": str,
        "thresholdCrossed": bool,
        "onTimeReporting": bool,
        "waiver": str,
        "financialOutcome": str,
        "note": Or(None, str),
        "creationDate": str
      }
    ],
    "total": int
  }
)


"""
  Schema atteso gli interfaccia POST /v1/riskaudit/waiver/cwmto/search (TC0030)
  response body: ListResultCwmtoSearchDTO
"""
ListResultCwmtoSearchDTO = Schema(
  {
    "data": [
      {
        "date": str,
        "legalEntity": {
          "abi": str,
          "name": str
        },
        "refYear": int,
        "assessmentType": str,
        "note": Or(None, str),
        "creationDate": str
      }
    ],
    "total": int
  }
)