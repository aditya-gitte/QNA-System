import os
import time
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import TextConverter, PDFToTextConverter, DocxToTextConverter, PreProcessor
from haystack.utils import fetch_archive_from_http
from haystack.nodes import ElasticsearchRetriever, TfidfRetriever
from haystack.nodes import FARMReader, TransformersReader
from haystack.pipelines import ExtractiveQAPipeline
from haystack.utils import print_answers
import json

def qna_converter(question,pdf):
  host = os.environ.get("ELASTICSEARCH_HOST", "localhost")

  document_store = ElasticsearchDocumentStore(
      host=host,
      username="",
      password="",
      index="document"
  )


  converter = PDFToTextConverter(remove_numeric_tables=True, valid_languages=["en"])
  doc_pdf = converter.convert(file_path=pdf, meta=None)[0]

  content_in_doc_pdf = doc_pdf.content

  preprocessor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=False,
    split_by="word",
    split_length=100,
    split_respect_sentence_boundary=True)
  
  dict1 = preprocessor.process([doc_pdf])
  retriever = TfidfRetriever(document_store=document_store)
  document_store.write_documents(dict1)
  reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)

  pipe = ExtractiveQAPipeline(reader, retriever)



  prediction = pipe.run(query=question, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 3}})

  #debugging
  # answer = print_answers(prediction, details="all")
  # json_answer=json.dumps(answer, default=str)
  
  return prediction


#testing
# print("starting python script")
# time.sleep(50)
# ans=qna_converter('When can the State Government revise a Regional Plan after it comes into operation?','app/The Maharashtra Regional And Town Planning Act (MRTP).pdf')
# ans2=json.dumps(ans, default=str)
# # print(ans2 )
# with open(f"Output.json", "w") as f:
#f.write(ans2)