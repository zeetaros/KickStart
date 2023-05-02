# Core Module
## Hashing
Test the hashing in terminal:   
while in the root directory, open `ipython`
```python
from core.hashing import Hasher

hashed_string = Hasher.get_password_hash("hello")
hashed_string
> '$2b$12$usfUKCkvzbE0xlZdC9CwzOu7Npx3K9MowDclebDrzK9JqpGBlvYaa'

Hasher.verify_password("hello", hashed_string)
> True
Hasher.verify_password("helo", hashed_string)
> False
```