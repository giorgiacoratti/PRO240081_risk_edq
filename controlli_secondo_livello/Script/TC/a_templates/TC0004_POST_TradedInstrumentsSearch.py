## Descrizione: Lanciare POST /v1/riskaudit/{abi}/templates/templateC/traded-instruments/search con request body SearchParameters e parametro di query non obbligatorio
## Risultato atteso: 200 OK con response body ListResultTemplateCTradedInstrumentsSearchDTO

## Importante: è giusto che questa chiamata risponda con body vuoto

import utils, constants, json, templates, templates_response_schemas

expected_status_code = constants.OK_200
body_file_path = './TestData/requests/body/TC0004_post_traded_instrument_search.json'
query_param_file_path = './TestData/requests/query_parameters/TC0004_post_traded_instruments_search_query.json'

def TC0004_POST_TradedInstrumentsSearch():
  
  ## Importo le project variables, estraggo il body dal file .json e lo converto in obj per verificarne il formato 
  Log.Message('--- STEP 0: Estrazione dei query parameters dal file '+query_param_file_path+', estraggo il body dal file '+body_file_path+' e importo le project variables ---')
  
  if Project.Variables.abi:
    abi = Project.Variables.abi
  else: 
    Log.Error('abi non presente tra le project variables, verificare!')
    
  body_obj = utils.JSON_file_to_obj(body_file_path)

  ## Chiamo il servizio
  Log.Message('--- STEP 1: Chiamata al servizio')
  
  Log.Message('Request body: '+json.dumps(body_obj, default=str, indent=4))
  
  resp = templates.POST_traded_instruments_search(body_obj, abi)
  
  ## Verifico e leggo lo status code 
  if resp.StatusCode != expected_status_code:
    if resp.Text:
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
    
      schema = templates_response_schemas.ListResultTemplateCTradedInstrumentsSearchDTO
    
      if not utils.validate(schema, response_body_dict):
        Log.Warning('La risposta del servizio NON rispetta lo schema atteso, verificare')
        Log.Warning('Response body: '+json.dumps(response_body_dict, default=str, indent=4))
        Log.Warning('Schema atteso: '+json.dumps(schema, default=str, indent=4))
        
      else:
        
        Log.Message('La response del servizio rispetta lo schema atteso ListResultTemplateCTradedInstrumentsSearchDTO')        
        Log.Message('Item restituito: '+json.dumps(response_body_dict, default=str, indent=4))