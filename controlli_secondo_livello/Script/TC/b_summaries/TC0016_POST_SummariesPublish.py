## Descrizione: Lanciare POST /v1/riskaudit/summaries/publish
## Risultato atteso: 200 OK

## Descrizione: 

import utils, constants, json, summaries

expected_status_code = constants.OK_200

def TC0016_POST_SummariesPublish():

  ## Chiamo il servizio
  Log.Message('--- STEP 1: Chiamata al servizio')
  
  resp = summaries.POST_summaries_publish()
  
  ## Verifico e leggo lo status code 
  if resp.StatusCode != expected_status_code:
    if resp.Text:
      Log.Warning('Messaggio di errore: '+resp.Text)
    Log.Error('Response status NON CORRETTO. Lo status PREVISTO era: '+str(expected_status_code))
  else:
    Log.Message('Response status CORRETTO.')