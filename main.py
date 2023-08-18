import os
import re
from PyPDF2 import PdfReader

folder_location = "Your folder location"
counter_all = 0
counter_renamed = 0

for filename in os.listdir(folder_location) :
  if filename.endswith('.pdf'):
    file_path = os.path.join(folder_location, filename)

    try:
      reader = PdfReader(file_path)
      page = reader.pages[0]
      text = page.extract_text()
      
      year_match = re.search(r'\d{4}', text)
      company_match = re.search(r'PT .+', text)

      if year_match and company_match :
          company = company_match.group().strip()
          year = year_match.group().strip()
          os.rename(file_path, os.path.join(folder_location, year+ ' - '+company+'.pdf'))
          counter_renamed += 1
          print(file_path+' renamed')

    except:
        continue
    counter_all += 1

print('Renaming done. '+str(counter_renamed)+' files renamed from '+str(counter_all)+' files.')
  





