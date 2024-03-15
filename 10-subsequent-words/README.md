<h1>10. Subsequent words</h1>

<h2>Function: <code>words_with_letters(words, letters)</code></h2>

<p>
  This problem serves as an excuse to introduce some general discrete math terminology that will 
  help make many later problem specifications less convoluted and ambiguous. A substring of a  
  string consists of characters taken in order from consecutive positions. Contrast this with the  
  similar concept of subsequence of characters still taken in order, but not necessarily at  
  consecutive positions. For example, each of the five strings '', 'e', 'put', 'ompu' and  
  'computer' is both a substring and subsequence of the string 'computer', whereas 'cper' and  
  'out' are subsequences, but not substrings. </p>
<p>
  Note how the empty string is always a substring of every possible string, including itself.  
  Every string is always its own substring, although not a proper substring the same way how all  
  other substrings are proper. Concepts of sublist and subsequence are defined for lists in an  
  analogous manner. Since sets have no internal order on top of the element membership in that  
  set, sets can meaningfully have both proper and improper subsets. (The concept of “subsetquence”  
  might mean a subset that would be a subsequence, were the members of that set were written out  
  sequentially in sorted order. But that term was just made up ad hoc for its comical value.) </p>
<p>
  Now that you know all that, given a list of words sorted in alphabetical order, and a string of  
  required letters, find and return the list of words that contain letters as a subsequence. 
</p>

<h3>Examples:</h3>

<table>
  <thead>
    <tr>
      <th>letters</th>
      <th>Expected Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>'klore'</td>
      <td>['booklore', 'booklores', 'folklore', 'folklores', 
          'kaliborite', 'kenlore', 'kiloampere', 'kilocalorie', 
          'kilocurie', 'kilogramme', 'kilogrammetre', 'kilolitre', 
          'kilometrage', 'kilometre', 'kilooersted', 'kiloparsec', 
          'kilostere', 'kiloware']</td>
    </tr>
    <tr>
      <td>'brohiic'</td>
      <td>['bronchiectatic', 'bronchiogenic', 'bronchitic', 
          'ombrophilic', 'timbrophilic']</td>
    </tr>
    <tr>
      <td>'azaz'</td>
      <td>['azazel', 'azotetrazole', 'azoxazole', 
          'diazoaminobenzene', 'hazardize', 'razzmatazz']</td>
    </tr>
  </tbody>
</table>
