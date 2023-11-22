<h1>8. Count Dominators</h1>

<h2>Function: <code>count_dominators(items)</code></h2>

<p>
  Define an element of a list of items to be a dominator if every element to its right (not just the one element that is immediately to its right) is strictly smaller than that element. Note how according to this definition, the last item of the list is automatically a dominator, regardless of its value. This function should return the count of how many elements in items are dominators.
</p>

<p>
  For example, the dominators of the list [42, 7, 12, 9, 13, 5] would be 42, 13, and 5. Regardless of its value, the last element of the list is trivially a dominator, since nothing greater follows it in the list.
</p>

<p>
  Before starting to write code for this function, you should consult the parable of “Shlemiel the painter” and think how this seemingly silly tale from a simpler time relates to today’s computational problems performed on lists, strings, and other sequences. This problem will be the first of many that you will encounter during and after this course to illustrate the important principle of using only one loop to achieve in a tiny fraction of time the same end result that Shlemiel achieves with two nested loops. Your workload, therefore, increases only linearly with respect to the number of items, whereas the total time of Shlemiel’s back-and-forth grows quadratically, that is, as a function of the square of the number of items.
</p>

<p>
  Trying to hide the inner loop of some Shlemiel algorithm inside a function call (this includes Python built-ins such as max and list slicing) and pretending that this somehow makes those inner loops take a constant time will only summon the Gods of Compubook Headings to return with tumult to claim their lion’s share of execution time.
</p>

<h3>Example:</h3>

<table>
  <thead>
    <tr>
      <th>items</th>
      <th>Expected Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[42, 7, 12, 9, 2, 5]</td>
      <td>4</td>
    </tr>
    <tr>
      <td>[]</td>
      <td>0</td>
    </tr>
    <tr>
      <td>[-2, 5, -1, -3]</td>
      <td>3</td>
    </tr>
    <tr>
      <td>[-10, -20, -30, -42]</td>
      <td>4</td>
    </tr>
    <tr>
      <td>[42, 42, 42, 42]</td>
      <td>1</td>
    </tr>
    <tr>
      <td>range(10**7)</td>
      <td>1</td>
    </tr>
    <tr>
      <td>range(10**7, 0, -1)</td>
      <td>10000000</td>
    </tr>
  </tbody>
</table>