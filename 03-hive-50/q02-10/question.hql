-- 
-- Pregunta
-- ===========================================================================
--
-- Para resolver esta pregunta use el archivo `data.tsv`.
--
-- Construya una consulta que ordene la tabla por letra y valor (3ra columna).
--
-- Escriba el resultado a la carpeta `output` de directorio de trabajo.
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
DROP TABLE IF EXISTS data;
DROP TABLE IF EXISTS ordena;

CREATE TABLE data (letra STRING, fecha DATE, numero INT) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'; 

LOAD DATA LOCAL INPATH "data.tsv" OVERWRITE INTO TABLE data;

CREATE TABLE ordena
AS
    SELECT *
    FROM
        data

ORDER BY
    letra, numero, fecha;

INSERT OVERWRITE LOCAL DIRECTORY 'output'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM ordena;
