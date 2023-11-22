<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Colour Trio</title>
</head>
<body>

<h1>7. Colour Trio</h1>

<h2>Function: <code>colour_trio(colours)</code></h2>

<p>
  This problem was inspired by the Mathologer video “Secret of Row 10”. To start, assume the existence of three values called “red”, “yellow” and “blue”. These names serve as colourful (heh) mnemonics and could as well have been 0, 1, and 2, or “foo”, “bar” and “baz”; no connection to actual physical colours is implied.
  Next, define a rule to mix such colours so that mixing any colour with itself gives that same colour, whereas mixing any two different colours always gives the third colour. For example, mixing blue to blue gives that same blue, whereas mixing blue to yellow gives red, same as mixing yellow to blue, or red to red. </p>
<p>
  Given the first row of colours as a string of lowercase letters, this function should construct the rows below the first row one row at the time according to the following discipline. Each row is one element shorter than the previous row. The i:th element of each row comes from mixing the colours in positions i and i + 1 of the previous row. Rinse and repeat until only the singleton element of the bottom row remains, returned as the final answer.
</p>

<h3>Examples:</h3>

<table>
  <thead>
    <tr>
      <th>colours</th>
      <th>Expected Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>'y'</td>
      <td>'y'</td>
    </tr>
    <tr>
      <td>'bb'</td>
      <td>'b'</td>
    </tr>
    <tr>
      <td>'rybyry'</td>
      <td>'r'</td>
    </tr>
    <tr>
      <td>'brybbr'</td>
      <td>'r'</td>
    </tr>
    <tr>
      <td>'rbyryrrbyrbb'</td>
      <td>'y'</td>
    </tr>
    <tr>
      <td>'yrbbbbryyrybb'</td>
      <td>'b'</td>
    </tr>
  </tbody>
</table>

</body>
</html>
