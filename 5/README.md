<h1>5. Cyclops Numbers</h1>

<h2>Function: <code>is_cyclops(n)</code></h2>

<p>
  A nonnegative integer is said to be a cyclops number if it consists of an odd number of digits so
  that the middle (more poetically, the “eye”) digit is a zero, and all the other digits of that number are
  non-zero. This function should determine whether its parameter integer <code>n</code> is a cyclops number,
  and return either <code>True</code> or <code>False</code> accordingly.
</p>

<h3>Examples:</h3>

<table>
  <thead>
    <tr>
      <th>n</th>
      <th>Expected Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>True</td>
    </tr>
    <tr>
      <td>101</td>
      <td>True</td>
    </tr>
    <tr>
      <td>98053</td>
      <td>True</td>
    </tr>
    <tr>
      <td>777888999</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1056</td>
      <td>False</td>
    </tr>
    <tr>
      <td>675409820</td>
      <td>False</td>
    </tr>
  </tbody>
</table>

<h3>Additional Challenge:</h3>

<p>
  As an extra challenge, you can try to solve this problem using only loops, conditions, and integer
  arithmetic operations, without first converting the integer into a string and working from there.
</p>

<p>
  Dividing any integer by 10 using the integer division <code>//</code> effectively chops off its last digit, whereas extracting
  the remainder of dividing by 10 using the operator <code>%</code> will extract that last digit. These operations allow us to iterate
  through the digits of an integer one at a time from lowest to highest, almost as if that integer really were some kind of
  sequence of digits.
</p>

<p>
  Even better, this operation doesn’t work merely for the familiar base ten, but it works for any base by using that base
  as the divisor. Especially using two as the divisor instead of ten allows you to iterate through the bits of the binary
  representation of any integer, which will come in handy in problems in your later courses that expect you to be able to
  manipulate these individual bits. (In practice, these division and remainder operations are often further condensed into
  equivalent but faster bit shifts and bitwise and operations.)
</p>