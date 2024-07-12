<body>
    <h1>12. Exact change only</h1>
    <pre>
def give_change(amount, coins):
    </pre>
    <p>
        Given the amount of money, expressed as the total number of kopecks of Latveria, Ruritania, Montenegro or some other one of those such vaguely Slavic fictional countries that Tintin and similar hearty fellows like to visit for a wacky chase to grab the current year’s MacGuffin, followed by the list of available denominations of coins also expressed as kopecks, this function should create and return a list of coins that add up to the amount using the greedy approach where you use as many of the highest denomination coins when possible before moving on to the next lower denomination. The list of coin denominations is guaranteed to be given in descending sorted order, as should your returned result also be.
    </p>
    <table border="1">
        <thead>
            <tr>
                <th>amount</th>
                <th>coins</th>
                <th>Expected result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>64</td>
                <td>[50, 25, 10, 5, 1]</td>
                <td>[50, 10, 1, 1, 1, 1]</td>
            </tr>
            <tr>
                <td>123</td>
                <td>[100, 25, 10, 5, 1]</td>
                <td>[100, 10, 10, 1, 1, 1]</td>
            </tr>
            <tr>
                <td>100</td>
                <td>[42, 17, 11, 6, 1]</td>
                <td>[42, 42, 11, 1, 1, 1, 1, 1]</td>
            </tr>
        </tbody>
    </table>
    <p>
        Along with its countless variations, this problem is a computer science classic when modified to minimize the total number of returned coins. The above greedy approach then no longer produces the optimal result for all possible coin denominations. For example, using the simple coin denominations of [50, 30, 1] and the amount of sixty kopecks to be exchanged, the greedy solution [50, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ends up using eleven coins due to the unfortunate first choice that prevents it from using any of the 30-kopeck coins. Those 30-kopeck coins sure would come handy here, seeing that the optimal solution [30, 30] needs only two such coins! A more advanced recursive algorithm examines both sides of the “take it or leave it” decision for each coin and chooses the choice that ultimately leads to a superior outcome. The intermediate results of this recursion should then be memoized to avoid blowing up the running time exponentially.
    </p>
</body>