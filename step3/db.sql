CREATE TABLE operadoras (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(100),
    representante VARCHAR(100),
    cargo_representante VARCHAR(100),
    regiao_de_comercializacao VARCHAR(100),
    data_registro_ans DATE
);

CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans VARCHAR(20),
    data DATE,
    conta_contabil VARCHAR(50),
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(15, 2),
    vl_saldo_final DECIMAL(15, 2),
    FOREIGN KEY (registro_ans) REFERENCES operadoras (registro_ans)
);

LOAD DATA LOCAL INFILE './Relatorio_cadop.csv' INTO
TABLE operadoras CHARACTER SET latin1 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (
    registro_ans,
    cnpj,
    razao_social,
    nome_fantasia,
    modalidade,
    logradouro,
    numero,
    complemento,
    bairro,
    cidade,
    uf,
    cep,
    ddd,
    telefone,
    fax,
    email,
    representante,
    cargo_representante,
    @regiao_de_comercializacao,
    @data_registro_ans
)
SET
    data_registro_ans = CASE
        WHEN @data_registro_ans REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$' THEN STR_TO_DATE(
            @data_registro_ans,
            '%d/%m/%Y'
        )
        WHEN @data_registro_ans REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' THEN @data_registro_ans
        ELSE NULL
    END,
    regiao_de_comercializacao = NULLIF(
        @regiao_de_comercializacao,
        ''
    );

LOAD DATA LOCAL INFILE './1T2023.csv' INTO
TABLE demonstracoes_contabeis FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data,
    registro_ans,
    conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    data = CASE
                                WHEN @data REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$' THEN STR_TO_DATE(
                                        @data,
                                        '%d/%m/%Y'
                                                                                                   )
                                WHEN @data REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' THEN @data
                                ELSE NULL
            END,
    vl_saldo_inicial =
REPLACE (
        REPLACE (@vl_saldo_inicial, '.', ''),
            ',',
            '.'
    ),
    vl_saldo_final =
REPLACE (
        REPLACE (@vl_saldo_final, '.', ''),
            ',',
            '.'
    );

LOAD DATA LOCAL INFILE './2T2023.csv' INTO
TABLE demonstracoes_contabeis FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data,
    registro_ans,
    conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    data = CASE
        WHEN @data REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$' THEN STR_TO_DATE(@data, '%d/%m/%Y')
        WHEN @data REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' THEN @data
        ELSE NULL
    END,
    vl_saldo_inicial =
REPLACE (
        REPLACE (@vl_saldo_inicial, '.', ''),
            ',',
            '.'
    ),
    vl_saldo_final =
REPLACE (
        REPLACE (@vl_saldo_final, '.', ''),
            ',',
            '.'
    );

LOAD DATA LOCAL INFILE './3T2023.csv' INTO
TABLE demonstracoes_contabeis FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data,
    registro_ans,
    conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    data = CASE
        WHEN @data REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$' THEN STR_TO_DATE(@data, '%d/%m/%Y')
        WHEN @data REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' THEN @data
        ELSE NULL
    END,
    vl_saldo_inicial =
REPLACE (
        REPLACE (@vl_saldo_inicial, '.', ''),
            ',',
            '.'
    ),
    vl_saldo_final =
REPLACE (
        REPLACE (@vl_saldo_final, '.', ''),
            ',',
            '.'
    );

LOAD DATA LOCAL INFILE './4T2023.csv' INTO
TABLE demonstracoes_contabeis FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data,
    registro_ans,
    conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    data = CASE
        WHEN @data REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$' THEN STR_TO_DATE(@data, '%d/%m/%Y')
        WHEN @data REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' THEN @data
        ELSE NULL
    END,
    vl_saldo_inicial =
REPLACE (
        REPLACE (@vl_saldo_inicial, '.', ''),
            ',',
            '.'
    ),
    vl_saldo_final =
REPLACE (
        REPLACE (@vl_saldo_final, '.', ''),
            ',',
            '.'
    );

LOAD DATA LOCAL INFILE './1T2024.csv' INTO
TABLE demonstracoes_contabeis FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data,
    registro_ans,
    conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    data = CASE
        WHEN @data REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$' THEN STR_TO_DATE(@data, '%d/%m/%Y')
        WHEN @data REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' THEN @data
        ELSE NULL
    END,
    vl_saldo_inicial =
REPLACE (
        REPLACE (@vl_saldo_inicial, '.', ''),
            ',',
            '.'
    ),
    vl_saldo_final =
REPLACE (
        REPLACE (@vl_saldo_final, '.', ''),
            ',',
            '.'
    );

LOAD DATA LOCAL INFILE './2T2024.csv' INTO
TABLE demonstracoes_contabeis FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data,
    registro_ans,
    conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    data = CASE
        WHEN @data REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$' THEN STR_TO_DATE(@data, '%d/%m/%Y')
        WHEN @data REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' THEN @data
        ELSE NULL
    END,
    vl_saldo_inicial =
REPLACE (
        REPLACE (@vl_saldo_inicial, '.', ''),
            ',',
            '.'
    ),
    vl_saldo_final =
REPLACE (
        REPLACE (@vl_saldo_final, '.', ''),
            ',',
            '.'
    );

LOAD DATA LOCAL INFILE './3T2024.csv' INTO
TABLE demonstracoes_contabeis FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data,
    registro_ans,
    conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    data = CASE
        WHEN @data REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$' THEN STR_TO_DATE(@data, '%d/%m/%Y')
        WHEN @data REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' THEN @data
        ELSE NULL
    END,
    vl_saldo_inicial =
REPLACE (
        REPLACE (@vl_saldo_inicial, '.', ''),
            ',',
            '.'
    ),
    vl_saldo_final =
REPLACE (
        REPLACE (@vl_saldo_final, '.', ''),
            ',',
            '.'
    );

LOAD DATA LOCAL INFILE './4T2024.csv' INTO
TABLE demonstracoes_contabeis FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data,
    registro_ans,
    conta_contabil,
    descricao,
    @vl_saldo_inicial,
    @vl_saldo_final
)
SET
    data = CASE
        WHEN @data REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$' THEN STR_TO_DATE(@data, '%d/%m/%Y')
        WHEN @data REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' THEN @data
        ELSE NULL
    END,
    vl_saldo_inicial =
REPLACE (
        REPLACE (@vl_saldo_inicial, '.', ''),
            ',',
            '.'
    ),
    vl_saldo_final =
REPLACE (
        REPLACE (@vl_saldo_final, '.', ''),
            ',',
            '.'
    );

WITH
    ultimo_trimestre AS (
        SELECT registro_ans, SUM(vl_saldo_final) AS total_despesas
        FROM demonstracoes_contabeis
        WHERE
            descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
            AND data BETWEEN '2024-10-01' AND '2024-12-31'
        GROUP BY
            registro_ans
    )
SELECT o.razao_social, o.nome_fantasia, ut.total_despesas
FROM
    ultimo_trimestre ut
    JOIN operadoras o ON ut.registro_ans = o.registro_ans
ORDER BY ut.total_despesas DESC
LIMIT 10;

WITH
    ultimo_ano AS (
        SELECT registro_ans, SUM(vl_saldo_final) AS total_despesas
        FROM demonstracoes_contabeis
        WHERE
            descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
            AND data BETWEEN '2024-01-01' AND '2024-12-31'
        GROUP BY
            registro_ans
    )
SELECT o.razao_social, o.nome_fantasia, ua.total_despesas
FROM ultimo_ano ua
    JOIN operadoras o ON ua.registro_ans = o.registro_ans
ORDER BY ua.total_despesas DESC
LIMIT 10;