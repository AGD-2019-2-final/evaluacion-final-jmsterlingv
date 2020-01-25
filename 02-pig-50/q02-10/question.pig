-- Pregunta
-- ===========================================================================
-- 
-- Ordene el archivo `data.tsv`  por letra y valor (3ra columna).
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
-- 
--  >>> Escriba el codigo del mapper a partir de este punto <<<
-- 
data = LOAD 'data.tsv' USING PigStorage('\t') 
    AS (letra:CHARARRAY, 
        fecha:CHARARRAY,
        cantidad:INT);
DUMP data;

x = ORDER data BY $0, $2;
DUMP x;

STORE x INTO 'output' using PigStorage('\t');