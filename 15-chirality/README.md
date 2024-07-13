<!DOCTYPE html>
<html>
<head>
    <title>15. Chirality</title>
</head>
<body>
    <h1>15. Chirality</h1>
    <pre>
def is_left_handed(pips):
    </pre>
    <p>
        Even though this has no effect on fairness, the pips from one to six are not painted on dice just any which way, but so that pips on the opposite faces always add up to seven. (This convention makes it easier to tell when someone tries to use crooked dice where certain undesirable pip values have been replaced with more amenable opposite values.) In each of the 2<sup>3</sup> = 8 corners of the cube, exactly one value from each pair of forbidden opposites 1–6, 2–5 and 3–4 meets two values chosen from the other two pairs of forbidden opposites. You can twist and turn any corner of the die to face you, and yet no two opposite sides ever come together into simultaneous view.
    </p>
    <p>
        This discipline still allows for two distinct ways to paint the pips. If the numbers in the corner shared by the faces 1, 2, and 3 read out clockwise as 1–2–3, that die is left-handed, whereas if they read out as 1–3–2, that die is right-handed. Analogous to a pair of shoes made separately for the left and right foot, the left- and right-handed dice are in one sense perfectly identical, and yet again no matter how you twist and turn either yourself or the show, you can’t seriously put either shoe in the other foot than the one it was designed for. (At least, not without taking that three-dimensional pancake “Through the Looking-Glass” by flipping it around in the fourth dimension!)
    </p>
    <p>
        The three numbers around any other corner determine the three numbers in the unseen opposite sides, and therefore also the handedness of that entire die just as firmly. Given the three-tuple of pips read clockwise around some corner, determine whether that die is left-handed. There are only 2<sup>3</sup> × 3! = 8 × 6 = 48 possible pip combinations to test for, so feel free to exploit these four two-fold symmetries to simplify your code. (The first four test cases below strongly hint at the nature of these symmetries, &lt;milhouse&gt;hint hint&lt;/milhouse&gt;.)
    </p>
    <table border="1">
        <thead>
            <tr>
                <th>Pips</th>
                <th>Expected Result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>(1, 2, 3)</td>
                <td>True</td>
            </tr>
            <tr>
                <td>(1, 5, 3)</td>
                <td>False</td>
            </tr>
            <tr>
                <td>(5, 3, 1)</td>
                <td>False</td>
            </tr>
            <tr>
                <td>(1, 3, 5)</td>
                <td>True</td>
            </tr>
            <tr>
                <td>(6, 5, 4)</td>
                <td>False</td>
            </tr>
        </tbody>
    </table>
    <p>
      This problem would certainly make for an interesting exercise of code golf, the propeller beanie discipline that we otherwise frown upon in this course as the falsest economy in coding. Also, after solving that one, imagine that our physical space had k dimensions, instead of merely just the familiar three. How would dice even be cast (in both senses of this word) in k dimensions? How would you generalize your function to find the chirality of an arbitrary k-dimensional die?
    </p>
</body>
</html>
