# Ascending List

## Problem Description
```python
def is_ascending(items):
```
Determine whether the sequence of items is strictly ascending so that each element is strictly larger (not just merely equal to) than the element that precedes it. Return True if the elements in the list of items are strictly ascending, and return False otherwise.

Note that the empty sequence is ascending, as is also every one-element sequence, so be careful to ensure that your function returns the correct answers in these seemingly insignificant edge cases of this problem. (If these sequences were not ascending, pray tell, what would be the two elements that violate the requirement and make that particular sequence not be ascending?)

<table>
  <thead>
    <tr>
      <th>Items</th>
      <th>Expected Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[]</td>
      <td>True</td>
    </tr>
    <tr>
      <td>[-5, 10, 99, 123456]</td>
      <td>True</td>
    </tr>
    <tr>
      <td>[2, 3, 3, 4, 5]</td>
      <td>False</td>
    </tr>
    <tr>
      <td>[-99]</td>
      <td>True</td>
    </tr>
    <tr>
      <td>[4, 5, 6, 7, 3, 7, 9]</td>
      <td>False</td>
    </tr>
    <tr>
      <td>[1, 1, 1, 1]</td>
      <td>False</td>
    </tr>
  </tbody>
</table>


In the same spirit, note how every possible universal claim made about the elements of an empty sequence is trivially true! For example, if `items` is the empty sequence, the two claims “All elements of `items` are odd” and “All elements of `items` are even” are both equally true, as is also the claim <br> “All elements of `items` are colorless green ideas that sleep furiously ([Colorless Green Ideas Sleep Furiously](https://en.wikipedia.org/wiki/Colorless_green_ideas_sleep_furiously))."