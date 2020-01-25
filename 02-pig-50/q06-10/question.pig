-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data = LOAD 'data.tsv' USING PigStorage('\t') 
    AS (letra:CHARARRAY, 
        bolsa:BAG{b:TUPLE(t:CHARARRAY)},
        mapa:MAP[]);
DUMP data;

x = FOREACH data GENERATE $2;
DUMP x;

y = FOREACH x GENERATE FLATTEN(mapa) AS let;
DUMP y;

z = GROUP y BY let;
DUMP z;

cuenta = FOREACH z GENERATE group, COUNT(y);
DUMP cuenta;

STORE cuenta INTO 'output' using PigStorage(',');