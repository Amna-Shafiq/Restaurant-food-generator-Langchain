from langchain.llms import OpenAI
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


os.environ['OPENAI_API_KEY']="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"
llm = OpenAI(temperature=0.7)
def generate_restaurant_name_and_items(cuisine):
  prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a {cuisine} food restaurant. Generate a name for it"

  )
  name_chain = LLMChain(llm=llm,prompt=prompt_template_name,output_key="restaurant_name")

  prompt_template_menu_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template="suggest some menu items for {restaurant_name}. return it as comma separated list."

  )
  menu_items_chain = LLMChain(llm=llm,prompt=prompt_template_menu_items,output_key="menu_items")

  chain = SequentialChain(
    chains =[name_chain,menu_items_chain],
    input_variables=['cuisine'],
    output_variables=['restaurant_name','menu_items']
  )
  response = chain({'cuisine':cuisine})
  return response

if __name__ =='__main__':
  print(generate_restaurant_name_and_items("Italian"))

  # return{
  #   'restaurant':"curry delight",
  #   'menu-items':"makhni chicken"
  # }