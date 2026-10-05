## Descrizione: Lanciare GET /v1/riskaudit/summaries/{id}/print
## Risultato atteso: 200 OK con response body una stringa

## Descrizione:

import utils, constants, json, summaries

expected_status_code = constants.OK_200

def TC0019_GET_SummariesPrint():
  
  ## Importo le project variables
  Log.Message('--- STEP 0: Importo le project variables ---')
  
  if Project.Variables.summaries_id:
    summaries_id = Project.Variables.summaries_id
  else: 
    Log.Error('summaries_id non presente tra le project variables, verificare!')
  
  ## Chiamo il servizio
  Log.Message('--- STEP 1: Chiamata al servizio')
  
  resp = summaries.GET_summaries_print(summaries_id)
  
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
      response_body_dict = json.dumps(resp.Text)  
      
      Log.Message('Item restituito: '+json.dumps(response_body_dict, default=str, indent=4))