<body>
    <h1>18. Sevens rule, zeros drool</h1>
    <pre>
def seven_zero(n):
    </pre>
    <p>
        Seven is considered a lucky number in Western cultures, whereas zero is what nobody wants to be. 
        Let us brie6ly bring these two opposites together without letting it become some kind of emergency 
        by looking at positive integers that consist of some solid sequence of sevens, followed by some 
        (possibly empty) solid sequence of zeros. Examples of integers of this form are 7, 7700, 77777, 
        77777700, and 70000000000000. A surprising theorem proves that for any positive integer n, 
        there exists some integer of such seven-zero form that is divisible by n. Therefore, there actually 
        exist in6initely many. (DUCY?) This function should 6ind the smallest such seven-zero integer. 
        Even though discrete math and number theory always help, this exercise is not about you coming up 
        with a clever symbolic formula and the proof of its correctness. This problem is about iterating 
        through the numbers of this constrained form of sevens and zeros ef6iciently in strictly ascending 
        order, so that the function can mechanistically 6ind the smallest working number of this form. How-
        ever, to speed up the search, we accept the result that whenever n is not divisible by either 2 or 5, 
        the smallest such number will always consist of some solid sequence of sevens with no zero digits 
        after them. This can speed up your search by an order of magnitude for such friendly values of n. 
    </p>
    <p>
        This logic might be best written as a generator to yield such numbers. The body of this generator 
        consists of two nested loops. The outer loop iterates through the number of digits d in the current 
        number. For each d, the inner loop iterates through all possible k from one to d to create a number 
        that begins with a block of k sevens, followed by a block of d-k zeros. Most of its work done inside 
        that helper generator, the seven_zero function itself will be short and sweet. 
    </p>
    <h2>Examples</h2>
    <table border="1">
        <thead>
            <tr>
                <th>n</th>
                <th>Expected result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>70</td>
                <td>70</td>
            </tr>
            <tr>
                <td>17</td>
                <td>7777777777777777</td>
            </tr>
            <tr>
                <td>42</td>
                <td>7770</td>
            </tr>
            <tr>
                <td>103</td>
                <td>7777777777777777777777777777777777</td>
            </tr>
            <tr>
                <td>77700</td>
                <td>77700</td>
            </tr>
            <tr>
                <td>2**50</td>
                <td>700000000000000000000000000000000000000000000000000</td>
            </tr>
            <tr>
                <td>12345</td>
                <td>(a behemoth that consists of 822 sevens, followed by a single zero)</td>
            </tr>
        </tbody>
    </table>
    <p>
        This problem is adapted from the excellent MIT Open Courseware online textbook “Mathematics for 
        Computer Science” (PDF link to the 2018 version for anybody interested) that, like so many other 
        non-constructive combinatorial proofs, uses the pigeonhole principle to prove that some solution 
        must exist for any integer n, but provides no clue of where to actually 6ind that solution. 
    </p>
</body>