## Descrizione: Lanciare PUT /v1/riskaudit/summaries/{subSectionId}/answers/{questionId} con request body SubSectionAnswerUpdateDTO
## Risultato atteso: 200 OK con response body GenericResponse

## Descrizione: 

import utils, constants, json, summaries, summaries_response_schemas

expected_status_code = constants.OK_200
body_file_path = './TestData/requests/body/TC0011_put_subsection_answers.json'

def TC0011_PUT_SubSectionAnswers():
  
  ## Importo le project variables, estraggo il body dal file .json e lo converto in obj per verificarne il formato 
  Log.Message('--- STEP 0: Estraggo il body dal file '+body_file_path+' e importo le project variables ---')
  
  if Project.Variables.subsection_id and Project.Variables.question_id :
    subsection_id = Project.Variables.subsection_id
    question_id = Project.Variables.question_id
  else: 
    Log.Error('subsection_id e question_id non presenti tra le project variables, verificare!')
    
  body_obj = utils.JSON_file_to_obj(body_file_path)

  ## Chiamo il servizio
  Log.Message('--- STEP 1: Chiamata al servizio')
  
  Log.Message('Request body: '+json.dumps(body_obj, default=str, indent=4))
  
  resp = summaries.PUT_subsection_answers(body_obj, subsection_id, question_id)
  
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
    
      schema = summaries_response_schemas.GenericResponse
    
      if not utils.validate(schema, response_body_dict):
        Log.Warning('La risposta del servizio NON rispetta lo schema atteso, verificare')
        Log.Warning('Response body: '+json.dumps(response_body_dict, default=str, indent=4))
        Log.Warning('Schema atteso: '+json.dumps(schema, default=str, indent=4))
        
      else:
        
        Log.Message('La response del servizio rispetta lo schema atteso GenericResponse')        
        Log.Message('Item restituito: '+json.dumps(response_body_dict, default=str, indent=4))