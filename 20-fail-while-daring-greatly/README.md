<body>
    <h1>20. Fail while daring greatly</h1>
    <pre>
def josephus(n, k):
    </pre>
    <p>
        The ancient world of swords and sandals “🎶back when men were made of iron and their ships were made of wood🎶” could occasionally be an entertainingly ribald and violent place, at least accord-ing to popular historical docudramas such as “300”, “Spartacus: Blood and Sand” and “300: Rise of an Empire”. During one particularly memorable incident, a group of zealots (yes, Lana, literally) found themselves surrounded by overwhelming Roman forces. To avoid capture and humiliating death by cruci6ixion, in their righteous zeal these men committed themselves to mass suicide in a scheme that ensured each man’s unwavering commitment to their 6inal shared fate. These zealots arranged themselves in a circle, used lots to choose a step size k, and then repeatedly counted kmen ahead, killed that man and removed his corpse from this grim circle, and kept going.
        
Being normal people instead of computer scientists, this deadly game of eeny-meeny-miney-moe is one-based, and continues until the last man standing is expected to fall on his own sword to com-plete this dance. Josephus would very much prefer to be that last man, since he has other ideas of surviving. Help him survive with a function that, given n and k, returns the list of the execution or-der so that these men know which places let them be the survivors who get to walk away from this grim circle. A cute mathematical solution instantly determines the survivor when k = 2. Unfortu-nately k can get arbitrarily large, even far exceeding the current number of men... if only to brie6ly excite us cold and timid souls, hollow men without chests, the rictus of our black lips gaped in gri-mace that sneers at the strong men who once stumbled.(To lighten up this hammy lament delivered in earnest while milking the invisible cow, we can also note the adorable feline generalization of this problem for beings with several lives that practically begs to be turned into a viral YouTube video.)
    </p>
    <h2>Examples</h2>
    <table border="1">
        <thead>
            <tr>
                <th>n</th>
                <th>k</th>
                <th>Expected result</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>4</td>
                <td>1</td>
                <td>[1, 2, 3, 4]</td>
            </tr>
            <tr>
                <td>4</td>
                <td>2</td>
                <td>[2, 4, 3, 1]</td>
            </tr>
            <tr>
                <td>10</td>
                <td>3</td>
                <td>[3, 6, 9, 2, 7, 1, 8, 5, 10, 4]</td>
            </tr>
            <tr>
                <td>8</td>
                <td>7</td>
                <td>[7, 6, 8, 2, 5, 1, 3, 4]</td>
            </tr>
            <tr>
                <td>30</td>
                <td>4</td>
                <td>[4, 8, 12, 16, 20, 24, 28, 2, 7, 13, 18, 23, 29, 5, 11, 19, 26, 3, 14, 22, 1, 15, 27, 10, 30, 21, 17, 25, 9, 6]</td>
            </tr>
            <tr>
                <td>10</td>
                <td>10**100</td>
                <td>[10, 1, 9, 5, 2, 8, 7, 3, 6, 4]</td>
            </tr>
        </tbody>
    </table>
</body>