import sys
sys.path.insert(0, "../lib")
## Importo la posizione della libreria schema perché non la trova più in automatico... capire perché!
#sys.path.append(r"./Python311/Lib")
sys.path.append(r"C:\Program Files (x86)\SmartBear\TestComplete 15\Bin\Extensions\Python\Python311\Lib")

from schema import Schema, Or, Optional


"""
  Schema atteso gli interfaccia PUT /v1/riskaudit/summaries/{summaryId}/answers (TC0009)
  response body: SummaryUpdateDTO
"""
SummaryUpdateDTO = Schema(
  {
    "answers": [
      {
        "answerId": int,
        "questionId": int,
        "modifiedTms": Or(None, str),
        "modifiedBy": Or(None, str)
      }
    ]
  }
)


"""
  Schema atteso gli interfaccia PUT /v1/riskaudit/summaries/{subSectionId}/questions (TC0010), PUT /v1/riskaudit/summaries/{subSectionId}/answers/{questionId} (TC0011)
         PUT /v1/riskaudit/summaries/{id}/note (TC0012), PUT /v1/riskaudit/summaries/state (TC0013)
  response body: GenericResponse
"""
GenericResponse = Schema(
  {
    "id": Or(int, None)
  }
)


"""
  Schema atteso gli interfaccia POST /v1/riskaudit/summaries/search (TC0015)
  response body: ListResultSummariesSearchDTO
"""
ListResultSummariesSearchDTO = Schema(
  {
    "data": [
      {
        "id": str,
        "legalEntity": {
          "abi": str,
          "name": str
        },
        "quarterDate": str,
        "result": str,
        "state": str
      }
    ],
    "total": int
  }
)


"""
  Schema atteso gli interfaccia GET /v1/riskaudit/summaries/{id} (TC0018)
  response body: SummaryDTO
"""
SummaryDTO = Schema(
  {
    "id": str,
    "legalEntity": {
      "abi": str,
      "name": str
    },
    "state": str,
    "result": str,
    "modifiedBy": str,
    "modifiedTms": str,
    "sections": [
      {
        "id": int,
        "name": str,
        "subsections": [
          {
            "id": int,
            "name": str,
            "questions": [
              {
                "id": int,
                "name": str,
                "answer": {
                  "id": int,
                  "name": str,
                  "note": Or(None, str),
                  "modifiedBy": Or(None, str),
                  "modifiedTms": Or(None, str)
                },
                "position": int,
                "prefilled": Or(None, bool)
              }
            ]
          }
        ]
      }
    ],
    "ccbNote": Or(None, str),
    "bankNote": Or(None, str),
    "quarterDate": str,
    "historical": bool
  }
)


"""
  Schema atteso gli interfaccia GET /v1/riskaudit/summaries/subsections (TC0020)
  response body: SubsectionItemDTO
"""
SubsectionItemDTO = Schema(
  [
    {
      "id": int,
      "name": str
    }
  ]
)


"""
  Schema atteso gli interfaccia GET /v1/riskaudit/summaries/stats (TC0021), GET /v1/riskaudit/summaries/stats/{date} (TC0022)
  response body: StatsDTO
"""
StatsDTO = Schema(
  {
    "toCompileNumber": int,
    "compiledNumber": int,
    "closedNumber": int,
    "quarterDate": Or(None, str),
    "publishDate": Or(None, str)
  }
)


"""
  Schema atteso gli interfaccia GET /v1/riskaudit/summaries/logs (TC0023)
  response body: LogDTO
"""
LogDTO = Schema(
  {
    "receivingDate": str,
    "uploadingDate": str,
    "creationDate": str
  }
)


"""
  Schema atteso gli interfaccia GET /v1/riskaudit/summaries/answers/{subsectionId} (TC0024)
  response body: QuestionWithAnswerDTO
"""
QuestionWithAnswerDTO = Schema(
  [
    {
      "id": int,
      "name": str,
      "position": int,
      "answers": [
        {
          "id": int,
          "name": str,
          "position": int,
          "regScore": Or(float, int),
          "virScore": Or(float, int)
        }
      ]
    }
  ]
)


"""
  Schema atteso gli interfaccia POST /v1/riskaudit/summaries (TC0014)
  response body: SummariesCreateDTO
"""
SummariesCreateDTO = Schema(
  {
    "message": str,
    "referenceDate": str,
    "createdCount": int,
    "createdIds": [
      str
    ]
  }
)