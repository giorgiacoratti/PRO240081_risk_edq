## Descrizione: Lanciare GET /v1/riskaudit/summaries/answers/{subsectionId} con parametro di query non obbligatorio
## Risultato atteso: 200 OK con response body QuestionWithAnswerDTO

## Descrizione:

import utils, constants, json, summaries, summaries_response_schemas

expected_status_code = constants.OK_200
#query_param_file_path = './TestData/requests/query_parameters/TC0024_get_summaries_answers.json'

def TC0024_GET_SummariesAnswers():
  
  ## Importo le project variables
  Log.Message('--- STEP 0: Importo le project variables ---')
  
  if Project.Variables.subsection_id:
    subsection_id = Project.Variables.subsection_id
  else: 
    Log.Error('subsection_id non presente tra le project variables, verificare!')
#    
#  query_param_obj = utils.JSON_file_to_obj(query_param_file_path)  
#  query_string = utils.obj_to_query_string(query_param_obj)
  
  ## Chiamo il servizio
  Log.Message('--- STEP 1: Chiamata al servizio')
  
  #resp = summaries.GET_summaries_answers('?'+query_string, subsection_id)
  resp = summaries.GET_summaries_answers(subsection_id)
  
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
    
      schema = summaries_response_schemas.QuestionWithAnswerDTO
    
      if not utils.validate(schema, response_body_dict):
        Log.Warning('La risposta del servizio NON rispetta lo schema atteso, verificare')
        Log.Warning('Response body: '+json.dumps(response_body_dict, default=str, indent=4))
        Log.Warning('Schema atteso: '+json.dumps(schema, default=str, indent=4))
        
      else:
        
        Log.Message('La response del servizio rispetta lo schema atteso QuestionWithAnswerDTO')        
        Log.Message('Item restituito: '+json.dumps(response_body_dict, default=str, indent=4))