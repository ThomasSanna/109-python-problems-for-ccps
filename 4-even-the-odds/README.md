<body>

<h1>Even the Odds</h1>

<h2>Function: <code>only_odd_digits(n)</code></h2>

<h3>Introduction</h3>
<p>
  Check that the given positive integer <code>n</code> contains only odd digits (1, 3, 5, 7, and 9) when it is written out.
  Return <code>True</code> if this is the case, and <code>False</code> otherwise. Note that this question is not asking
  whether the number <code>n</code> itself is odd or even. You, therefore, will have to look at every digit of the given
  number before you can proclaim that the number contains no even digits.
</p>

<h3>Digit Extraction</h3>
<p>
  To extract the lowest digit of a positive integer <code>n</code>, use the expression <code>n % 10</code>. To chop off the lowest
  digit and keep the rest of the digits, use the expression <code>n // 10</code>. Alternatively, if you don't want to be this fancy,
  you can first convert the number into a string and manipulate it with string operations.
</p>

<h2>Examples:</h2>

<table>
  <thead>
    <tr>
      <th>n</th>
      <th>Expected Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1357975313579</td>
      <td>True</td>
    </tr>
    <tr>
      <td>42</td>
      <td>False</td>
    </tr>
    <tr>
      <td>71358</td>
      <td>False</td>
    </tr>
    <tr>
      <td>0</td>
      <td>False</td>
    </tr>
  </tbody>
</table>

</body>