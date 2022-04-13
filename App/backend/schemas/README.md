# Schemas Module
A schema is used to validate date received and to reformat the data that are sent to the client (browser). Normally, a schema will be created correspondingly for each model (table).  
  
Pydantic is a python package that can be leveraged to verify data types in schemas. In additionally, pydantic can be used to restrict data to have only a litmited number of fields being passed back in the API response body. This is useful from the security point of view.  
