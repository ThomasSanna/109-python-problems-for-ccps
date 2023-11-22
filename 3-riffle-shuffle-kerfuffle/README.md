<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Riffle Shuffle Kerfuffle</title>
</head>
<body>

<h1>Riffle Shuffle Kerfuffle</h1>

<h2>Introduction</h2>
<p>
  Given a list of items whose length is guaranteed to be even (note that “oddly” enough, zero is an even number),
  create and return a list produced by performing a perfect riffle to the items by interleaving the items of the two halves
  of the list in an alternating fashion.
</p>

<h2>Riffle Shuffle Explanation</h2>
<p>
  When performing a perfect riffle shuffle, also known as the Faro shuffle, the list of items is split in two equal-sized halves,
  either conceptually or in actuality. The first two elements of the result are then the first elements of those halves.
  The next two elements of the result are the second elements of those halves, followed by the third elements of those halves,
  and so on up to the last elements of those halves. The parameter 'out' determines whether this function performs an out shuffle
  or an in shuffle that determines which half of the deck the alternating card is first taken from.
</p>

<h2>Examples</h2>
<table>
  <thead>
    <tr>
      <th>Tableau</th>
      <th>Items</th>
      <th>Out</th>
      <th>Expected Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[1, 2, 3, 4, 5, 6, 7, 8]</td>
      <td>True</td>
      <td>[1, 5, 2, 6, 3, 7, 4, 8]</td>
    </tr>
    <tr>
      <td>[1, 2, 3, 4, 5, 6, 7, 8]</td>
      <td>False</td>
      <td>[5, 1, 6, 2, 7, 3, 8, 4]</td>
    </tr>
    <tr>
      <td>[]</td>
      <td>True</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>['bob', 'jack']</td>
      <td>True</td>
      <td>['bob', 'jack']</td>
    </tr>
    <tr>
      <td>['bob', 'jack']</td>
      <td>False</td>
      <td>['jack', 'bob']</td>
    </tr>
  </tbody>
</table>

</body>
</html>
