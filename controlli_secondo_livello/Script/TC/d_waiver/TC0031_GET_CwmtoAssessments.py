## Descrizione: Lanciare GET /v1/riskaudit/waiver/cwmto/assessments
## Risultato atteso: 200 OK con response body un array di stringhe

## Descrizione:

import utils, constants, json, waiver

expected_status_code = constants.OK_200

def TC0031_GET_CwmtoAssessments():
    
  ## Chiamo il servizio
  Log.Message('--- STEP 1: Chiamata al servizio')
  
  resp = waiver.GET_cwmto_search()
  
  ## Verifico e leggo lo status code
  if resp.StatusCode != expected_status_code:
    if resp.Text != '':
      Log.Warning('Messaggio di errore: '+resp.Text)
    Log.Error('Response status NON CORRETTO. Lo status PREVISTO era: '+str(expected_status_code))
  else:
    Log.Message('Response status CORRETTO.')
    
    ## Verifico la response validandola contro lo schema atteso 
    ## Se sono presenti dati li salvo in variabili locali e li loggo 
    Log.Message('--- STEP 2: Validazione della response')
    
    if resp.Text == '':
      Log.Error('La response non contiene un body')
    else:
      response_body_dict = json.loads(resp.Text)  
      
      Log.Message('Item restituito: '+json.dumps(response_body_dict, default=str, indent=4))