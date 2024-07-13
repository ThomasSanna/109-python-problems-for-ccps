<!DOCTYPE html>
<html>
<head>
    <title>Words with Given Shape</title>
</head>
<body>
    <h1>Words with Given Shape</h1>
    <pre>
def words_with_given_shape(words, shape):
    </pre>
    <p>
        The shape of the given word of length n is a list of n – 1 integers, each one either –1, 0 or +1 to indicate whether the next letter following the letter in that position comes later (+1), is the same (0) or comes earlier (–1) in the alphabetical order of English letters. For example, the shape of the word 'hello' is [-1, +1, 0, +1], whereas the shape of 'world' is [-1, +1, -1, -1]. Find and return a list of all words that have that particular shape, listed in alphabetical order. Note that your function, same as all the other functions specified in this document that operate on lists of words, should not try to read the wordlist file words_sorted.txt, even though yes, Python makes this not just possible but yawningly easy with just a couple of lines of code. The tester script already reads in the entire wordlist and builds the list of words from there. Your function should use this given list of words without even caring which particular file it came from.
    </p>
    <table border="1">
        <thead>
            <tr>
                <th>Shape</th>
                <th>Expected result (using wordlist words_sorted.txt)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>[1, -1, -1, -1, 0, -1]</td>
                <td>['congeed', 'nutseed', 'outfeed', 'strolld']</td>
            </tr>
            <tr>
                <td>[1, -1, -1, 0, -1, 1]</td>
                <td>['axseeds', 'brogger', 'cheddar', 'coiffes', 'crommel', 'djibbah', 'droller', 'fligger', 'frigger', 'frogger', 'griffes', 'grogger', 'grommet', 'prigger', 'proffer', 'progger', 'proller', 'quokkas', 'stiffen', 'stiffer', 'stollen', 'swigger', 'swollen', 'twiggen', 'twigger']</td>
            </tr>
            <tr>
                <td>[0, 1, -1, 1]</td>
                <td>['aargh', 'eeler', 'eemis', 'eeten', 'oopak', 'oozes', 'sstor']</td>
            </tr>
            <tr>
                <td>[1, 1, 1, 1, 1, 1, 1]</td>
                <td>['aegilops']</td>
            </tr>
        </tbody>
    </table>
    <p>
      Curious students can take on as a recreational challenge to find the shape of length n – 1 that matches the largest number of words, for the possible values of n from 3 to 20. Alternatively, try to count how many possible shapes of length n – 1 do not match any words of length n at all. What is the shortest possible shape that does not match any of the words in our giant wordlist?
    </p>
</body>
</html>
