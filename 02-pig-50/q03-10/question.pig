-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data = LOAD 'data.tsv' USING PigStorage('\t') 
    AS (letra:CHARARRAY, 
        fecha:CHARARRAY,
        cantidad:INT);
DUMP data;

x = ORDER data BY $2;
DUMP x;

y = FOREACH x GENERATE $2;
DUMP y;

z = LIMIT y 5;
DUMP z;

STORE z INTO 'output';