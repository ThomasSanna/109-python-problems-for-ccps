```markdown
# Problem: Count Growlers

```python
def count_growlers(animals):
```

Let the strings `'cat'` and `'dog'` represent animals facing left, while `'tac'` and `'god'` represent the same animals facing right. In this modern age, this setup might sound like a meme or one of those TikTok videos you kids are always watching. Let's assume, perhaps unrealistically, that each animal—regardless of species—growls if it sees **strictly more dogs than cats** in the direction it is facing.

Given a list of such animals, return the count of how many are growling. In the examples below, growling animals are highlighted in green.

> Sometimes, like cops and robbers in a gritty Netflix action romp, problems and solutions can be hard to tell apart—it all depends on your perspective.

## Examples

| animals                                                                                                 | Expected result |
|---------------------------------------------------------------------------------------------------------|----------------|
| `['cat', 'dog']`                                                                                        | 0              |
| `['god', 'cat', 'cat', 'tac', 'tac', 'dog', 'cat', 'god']`                                              | 2              |
| `['dog', 'cat', 'dog', 'god', 'dog', 'god', 'dog', 'god', 'dog', 'dog', 'god', 'god', 'cat', 'dog', 'god', 'cat', 'tac']` | 11             |
| `['god', 'tac', 'tac', 'tac', 'tac', 'dog', 'dog', 'tac', 'cat', 'dog', 'god', 'cat', 'dog', 'cat', 'cat', 'tac']`        | 0              |

---
Page 32 of 132