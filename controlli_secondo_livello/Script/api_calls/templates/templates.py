import generic_calls, json

base_url = ProjectSuite.Variables.base_path
token = ProjectSuite.Variables.token_CC9025
base_url_prova_fede = ProjectSuite.Variables.base_url_prova_fede
token_prova_fede = ProjectSuite.Variables.token_prova_fede


""" 
  Metodo che crea una GET request e la invia all'endpoint al path
  /v1/riskaudit/{abi}/templates/{template}/note
  @param: abi
  @param: template
"""
def GET_template_note(abi, template) :
  path = '/v1/riskaudit/'+abi+'/templates/'+template+'/note'
  url = base_url+path
  return generic_calls.send_request_generic('GET', url, token, path)
  
  
  
""" 
  Metodo che crea una PUT request e la invia all'endpoint al path
  /v1/riskaudit/{abi}/templates/{template}/note
  @param: body_obj
  @param: abi
  @param: template
"""
def PUT_template_note(body_obj, abi, template) :
  path = '/v1/riskaudit/'+abi+'/templates/'+template+'/note'
  url = base_url+path
  body_string = json.dumps(body_obj)
  return generic_calls.send_request_generic('PUT', url, token, path, body=body_string)
  
  
  
############################################################## PROVA FEDE  
""" 
  Metodo che crea una GET request e la invia all'endpoint al path
  /additional-information/config
"""
def GET_prova_fede() :
  path = '/additional-information/config'
  url = base_url_prova_fede+path
  return generic_calls.send_request_generic('GET', url, token_prova_fede, path)
###################################################################################
  
  
  
""" 
  Metodo che crea una POST request e la invia all'endpoint al path
  /v1/riskaudit/{abi}/templates/{template}/export
  @param: body_obj
  @param: abi
  @param: template
"""
def POST_template_export(body_obj, abi, template) :
  path = '/v1/riskaudit/'+abi+'/templates/'+template+'/export'
  url = base_url+path
  body_string = json.dumps(body_obj)
  return generic_calls.send_request_generic('POST', url, token, path, body=body_string)
  
  
  
""" 
  Metodo che crea una POST request e la invia all'endpoint al path
  /v1/riskaudit/{abi}/templates/templateC/traded-instruments/search
  @param: body_obj
  @param: abi
"""
def POST_traded_instruments_search(body_obj, abi) :
  path = '/v1/riskaudit/'+abi+'/templates/templateC/traded-instruments/search'
  url = base_url+path
  body_string = json.dumps(body_obj)
  return generic_calls.send_request_generic('POST', url, token, path, body=body_string)
  
  
  
""" 
  Metodo che crea una POST request e la invia all'endpoint al path
  /v1/riskaudit/{abi}/templates/templateC/held-instruments/search
  @param: body_obj
  @param: abi
"""
def POST_held_instrument_search(body_obj, abi) :
  path = '/v1/riskaudit/'+abi+'/templates/templateC/held-instruments/search'
  url = base_url+path
  body_string = json.dumps(body_obj)
  return generic_calls.send_request_generic('POST', url, token, path, body=body_string)
  
  
  
""" 
  Metodo che crea una POST request e la invia all'endpoint al path
  /v1/riskaudit/{abi}/templates/templateB/search
  @param: body_obj
  @param: abi
"""
def POST_template_b_search(body_obj, abi) :
  path = '/v1/riskaudit/'+abi+'/templates/templateB/search'
  url = base_url+path
  body_string = json.dumps(body_obj)
  return generic_calls.send_request_generic('POST', url, token, path, body=body_string)
  
  
  
""" 
  Metodo che crea una POST request e la invia all'endpoint al path
  /v1/riskaudit/{abi}/templates/templateA/search
  @param: body_obj
  @param: abi
"""
def POST_template_a_search(body_obj, abi) :
  path = '/v1/riskaudit/'+abi+'/templates/templateA/search'
  url = base_url+path
  body_string = json.dumps(body_obj)
  return generic_calls.send_request_generic('POST', url, token, path, body=body_string)
  
  
  
""" 
  Metodo che crea una GET request e la invia all'endpoint al path
  /v1/riskaudit/{abi}/templates/templateB/waivers
  @param: query_parameters
  @param: abi
"""
def GET_template_b_waivers(query_parameters, abi) :
  path = '/v1/riskaudit/'+abi+'/templates/templateB/waivers'+query_parameters
  url = base_url+path
  return generic_calls.send_request_generic('GET', url, token, path)