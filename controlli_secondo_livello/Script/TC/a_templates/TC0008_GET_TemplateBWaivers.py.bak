## Descrizione: Lanciare GET /v1/riskaudit/{abi}/templates/templateB/waivers con parametro di query non obbligatorio
## Risultato atteso: 200 OK con response body un array di stringhe

## Descrizione:

import utils, constants, json, templates, templates_response_schemas

expected_status_code = constants.OK_200
query_param_file_path = './TestData/requests/query_parameters/TC0005_post_heald_instruments_search_query.json'

def TC0008_GET_TemplateBWaivers():
  
  ## Importo le project variables, estraggo il body dal file .json e lo converto in obj per verificarne il formato 
  Log.Message('--- STEP 0: Estraggo dei query parameters dal file '+query_param_file_path+' e importo le project variables ---')
  
  if Project.Variables.abi:
    abi = Project.Variables.abi
  else: 
    Log.Error('abi non presente tra le project variables, verificare!')
  
  query_param_obj = utils.JSON_file_to_obj(query_param_file_path)  
  query_string = utils.obj_to_query_string(query_param_obj)
    
  ## Chiamo il servizio
  Log.Message('--- STEP 1: Chiamata al servizio')
  
  resp = templates.GET_template_b_waivers('?'+query_string, abi)
  
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