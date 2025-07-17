## 22. Count the balls off the brass monkey

```python
def pyramid_blocks(n, m, h):
```

Mysteries of the pyramids have fascinated humanity through the ages. Instead of packing your machete and pith helmet to trek through deserts and jungles to raid the hidden treasures of the ancients like some Indiana Croft, or by gaining visions of enlightenment by intensely meditating under the apex set over a square base like some Deepak Veidt, this problem deals with something a bit more mundane; truncated brass monkeys of layers of discrete uniform spheres, in spirit of that spherical cow running in a vacuum.

Given that the top layer of the truncated brass monkey consists of `n` rows and `m` columns of spheres, and each solid layer immediately below the one above it always contains one more row and one more column, how many spheres in total make up this truncated brass monkey that has `h` layers?

This problem could be solved in a straightforward brute force fashion by mechanistically tallying up the spheres iterated through these layers. However, the just reward for naughty boys and girls who take such a blunt approach is to watch the automated tester take roughly a minute to terminate! Some creative use of discrete math and summation formulas gives an analytical closed form formula that makes the answers come out faster than you can snap your fingers simply by plugging the values of `n`, `m` and `h` into this formula.

| n      | m      | h      | Expected result         |
|--------|--------|--------|------------------------|
| 2      | 3      | 1      | 6                      |
| 2      | 3      | 10     | 570                    |
| 10     | 11     | 12     | 3212                   |
| 100    | 100    | 100    | 2318350                |
| 10**6  | 10**6  | 10**6  | 2333331833333500000    |

As an unrelated note, as nice as Python can be for casual coding by liberating us from all that low level nitty gritty, Wolfram is another great language with great online documentation. You can play around with this language for free on Wolfram Cloud to try out not just all the cool one-liners from the tutorials and documentation pages, but evaluate arbitrary mathematical expressions of your own making, for example `Sum[(n+i)(m+i), {i, 0, h-1}]`, all in a fully symbolic fashion.


### French

Les Mystères des pyramides ont fasciné l’humanité à travers les âges. Au lieu de préparer votre machette et votre casque colonial pour traverser déserts et jungles à la recherche des trésors cachés des anciens comme un Indiana Croft, ou d’atteindre l’illumination en méditant intensément sous l’apex posé sur une base carrée comme un Deepak Veidt, ce problème traite de quelque chose de plus banal : des pyramides tronquées de couches de sphères uniformes, dans l’esprit de cette vache sphérique évoluant dans le vide.

Étant donné que la couche supérieure de la pyramide tronquée comporte `n` rangées et `m` colonnes de sphères, et que chaque couche solide immédiatement en dessous contient toujours une rangée et une colonne de plus, combien de sphères au total composent cette pyramide tronquée de `h` couches ?

Ce problème peut être résolu de façon brute en comptant mécaniquement les sphères à travers ces couches. Cependant, cette approche prend beaucoup de temps ! Une utilisation créative des mathématiques discrètes et des formules de sommation permet d’obtenir une formule analytique qui donne la réponse instantanément en insérant simplement les valeurs de `n`, `m` et `h` dans cette formule.

| n      | m      | h      | Résultat attendu        |
|--------|--------|--------|------------------------|
| 2      | 3      | 1      | 6                      |
| 2      | 3      | 10     | 570                    |
| 10     | 11     | 12     | 3212                   |
| 100    | 100    | 100    | 2318350                |
| 10**6  | 10**6  | 10**6  | 2333331833333500000    |

Note sans rapport : aussi agréable que soit Python pour le codage occasionnel, Wolfram est un autre excellent langage avec une documentation en ligne très complète. Vous pouvez l’essayer gratuitement sur Wolfram Cloud pour tester des expressions mathématiques, par exemple `Sum[(n+i)(m+i), {i, 0, h-1}]`, de façon entièrement symbolique.