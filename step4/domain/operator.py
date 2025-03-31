from dataclasses import dataclass

@dataclass
class Operator:
    registro_ans: str
    cnpj: str
    razao_social: str
    nome_fantasia: str
    modalidade: str
    logradouro: str
    numero: str
    complemento: str
    bairro: str
    cidade: str
    uf: str
    cep: str
    ddd: str
    telefone: str
    fax: str
    endereco_eletronico: str
    representante: str
    cargo_representante: str
    data_registro_ans: str
    
    def to_dict(self):
        return {
            "Registro_ANS": self.registro_ans,
            "CNPJ": self.cnpj,
            "Razao_Social": self.razao_social,
            "Nome_Fantasia": self.nome_fantasia,
            "Modalidade": self.modalidade,
            "Logradouro": self.logradouro,
            "Numero": self.numero,
            "Complemento": self.complemento,
            "Bairro": self.bairro,
            "Cidade": self.cidade,
            "UF": self.uf,
            "CEP": self.cep,
            "DDD": self.ddd,
            "Telefone": self.telefone,
            "Fax": self.fax,
            "Endereco_eletronico": self.endereco_eletronico,
            "Representante": self.representante,
            "Cargo_Representante": self.cargo_representante,
            "Data_Registro_ANS": self.data_registro_ans
        }