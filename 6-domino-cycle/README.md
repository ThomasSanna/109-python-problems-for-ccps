<h1>6. Domino Cycle</h1>

<h2>Function: <code>domino_cycle(tiles)</code></h2>

<p>
  A single domino tile is represented as a two-tuple of its pip values, such as (2,5) or (6,6). This
  function should determine whether the given list of tiles forms a cycle so that each tile in the list
  ends with the exact same pip value that its successor tile starts with, the successor of the last tile
  being the first tile of the list since this is supposed to be a cycle instead of a chain. Return <code>True</code> if
  the given list of tiles forms such a cycle, and <code>False</code> otherwise.
</p>

<h3>Examples:</h3>

<table>
  <thead>
    <tr>
      <th>tiles</th>
      <th>Expected Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[(3, 5), (5, 2), (2, 3)]</td>
      <td>True</td>
    </tr>
    <tr>
      <td>[(4, 4)]</td>
      <td>True</td>
    </tr>
    <tr>
      <td>[]</td>
      <td>True</td>
    </tr>
    <tr>
      <td>[(2, 6)]</td>
      <td>False</td>
    </tr>
    <tr>
      <td>[(5, 2), (2, 3), (4, 5)]</td>
      <td>False</td>
    </tr>
    <tr>
      <td>[(4, 3), (3, 1)]</td>
      <td>False</td>
    </tr>
  </tbody>
</table>