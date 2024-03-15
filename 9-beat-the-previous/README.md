<h1>9. Beat the Previous</h1>

<h2>Function: <code>extract_increasing(digits)</code></h2>

<p>
  Given a string of digits guaranteed to only contain ordinary integer digit characters 0 to 9, create and return the list of increasing integers acquired from reading these digits in order from left to right. The first integer in the result list is made up from the first digit of the string. After that, each element is an integer that consists of as many following consecutive digits as are needed to make that integer strictly larger than the previous integer. The leftover digits at the end of the digit string that do not form a sufficiently large integer are ignored.
</p>

<p>
  This problem can be solved with a for-loop through the digits that looks at each digit exactly once regardless of the position of that digit in the beginning, end, or middle of the string. Keep track of the current number (initially zero) and the previous number to beat (initially equal to minus one). Each digit d is then processed by pinning it at the end of the current number with the assignment <code>current=10*current+int(d)</code>, updating the result and previous as needed.
</p>

<h3>Examples:</h3>

<table>
  <thead>
    <tr>
      <th>digits</th>
      <th>Expected Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>'600005'</td>
      <td>[6]</td>
    </tr>
    <tr>
      <td>'045349'</td>
      <td>[0, 4, 5, 34]</td>
    </tr>
    <tr>
      <td>'77777777777777777777777'</td>
      <td>[7, 77, 777, 7777, 77777, 777777]</td>
    </tr>
    <tr>
      <td>'122333444455555666666'</td>
      <td>[1, 2, 23, 33, 44, 445, 555, 566, 666]</td>
    </tr>
    <tr>
      <td>'2718281828459045235360287 47135266249775724709369995 95749669676277240766303535 47594571382178525166427427 46639193200305992181741359 6629043572900334295260'</td>
      <td>[2, 7, 18, 28, 182, 845, 904, 5235, 36028, 74713, 526624, 977572, 4709369, 9959574, 96696762, 772407663, 3535475945, 7138217852, 51664274274, 66391932003, 599218174135, 966290435729]</td>
    </tr>
    <tr>
      <td>'1234' * 100</td>
      <td>A list with 38 elements, the last one equal to 341234123412341234123</td>
    </tr>
  </tbody>
</table>
