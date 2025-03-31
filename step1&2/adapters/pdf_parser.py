import pandas as pd
import pdfplumber

class PDFParser:
    def extract_table(self, pdf_path):
        expected_columns = [
            "PROCEDIMENTO", "RN", "VIGENCIA", 
            "OD", "AMB", "HCO", "HSO", "REF", "PAC", 
            "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
        ]
        
        data = []
        header = None 
        
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                
                if not table:
                    continue
                
                if not header:
                    header = table[0]
                    data.extend(table[1:])
                else:
                    if table[0] == header:
                        data.extend(table[1:])
                    else:
                        data.extend(table)
        
        return pd.DataFrame(data, columns=expected_columns)