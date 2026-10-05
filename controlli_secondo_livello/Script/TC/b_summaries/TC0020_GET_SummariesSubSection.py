## Descrizione: Lanciare GET /v1/riskaudit/summaries/subsections
## Risultato atteso: 200 OK con response body SubsectionItemDTO

## Descrizione:

import utils, constants, json, summaries, summaries_response_schemas

expected_status_code = constants.OK_200

def TC0020_GET_SummariesSubSection():
  
  ## Chiamo il servizio
  Log.Message('--- STEP 1: Chiamata al servizio')
  
  resp = summaries.GET_summaries_subsections()
  
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
    
      schema = summaries_response_schemas.SubsectionItemDTO
    
      if not utils.validate(schema, response_body_dict):
        Log.Warning('La risposta del servizio NON rispetta lo schema atteso, verificare')
        Log.Warning('Response body: '+json.dumps(response_body_dict, default=str, indent=4))
        Log.Warning('Schema atteso: '+json.dumps(schema, default=str, indent=4))
        
      else:
        
        Log.Message('La response del servizio rispetta lo schema atteso SubsectionItemDTO')        
        Log.Message('Item restituito: '+json.dumps(response_body_dict, default=str, indent=4))
        
        if response_body_dict[0]['id']:
          Project.Variables.subsection_id = response_body_dict[0]['id']
          Log.Message('E\' stata salvata la sottosessione con id: '+str(Project.Variables.subsection_id))
        else:
          Log.Error('Non è stato restituito nessun id, verificare!')