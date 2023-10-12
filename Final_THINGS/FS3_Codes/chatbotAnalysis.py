import pandas as pd
import itertools
import ebuddy
import openpyxl
from sentence_transformers import SentenceTransformer, util
class chatBotResponseAnalysis:
    
    def export_data_to_cvs(data):
        excel_data= pd.read_excel('Semantic_Analysis_Ebuddy.xlsx', sheet_name='Sheet1')

        questions = excel_data['Questions'].tolist()
        chatbot_answers = []
      
        for i in questions:
            #chatbot_answers.append(ebuddy.ask_ebuddy(i).strip())
            a = None
        chatbot_questions_data = {
            "Chatbot Response" : chatbot_answers
        }
        '''df = pd.DataFrame(chatbot_questions_data)
        with pd.ExcelWriter('Semantic_Analysis_Ebuddy.xlsx',mode='a') as writer:  
            df.to_excel(writer, sheet_name='Sheet2', index=False)'''
            
        semantic_analysis_data = {
            "Semantic Textual Similarity Score" : data
        }
        df = pd.DataFrame(semantic_analysis_data)
        with pd.ExcelWriter('Semantic_Analysis_Ebuddy.xlsx',mode='a') as writer:  
            df.to_excel(writer, sheet_name='Sheet3', index=False)
        

    def semantic_textual_similarity():
        semantic_textual_similarity_list = []
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        
        excel_data = pd.read_excel('Semantic_Analysis_Ebuddy.xlsx', sheet_name='Sheet2')
        excel_data_2 = pd.read_excel('Semantic_Analysis_Ebuddy.xlsx', sheet_name='Sheet1')
        
        chat_bot_answers = excel_data['Chatbot Response'].tolist()
        real_answers = excel_data_2['Answers'].tolist()
        
        for (i, j) in zip(chat_bot_answers, real_answers):
            embedding_of_chat_bot_answer= model.encode(i, convert_to_tensor=True)
            embedding_of_real_answer = model.encode(j, convert_to_tensor=True)
            tensor_value = util.pytorch_cos_sim(embedding_of_chat_bot_answer, embedding_of_real_answer)
            semantic_textual_similarity_list.append(tensor_value.item())
            #print(tensor_value.item())
        return semantic_textual_similarity_list
    data = semantic_textual_similarity() 
    export_data_to_cvs(data)
      
