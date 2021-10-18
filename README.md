## Refactoring Practice

Copy this template repository to your own Github account. Then clone it to your computer and do the refactorings.  Push your work to Github.

Each subdirectory contains some code that needs refactoring.

1. In this README, write one line describing each refactoring you apply and why.
2. Perform the refactoring in the subdirectory code.


## `time/timestamp.py`

Refactor timestamp.py.  2 or 3 refactorings are possible.

### Refactored list
- renamed method `createTimeFromTimestamp` to `create_time_from_timestamp` to match with PEP8 styles.
- extract method to `is_valid_time` to check valid time.
- remove else condition.


## `game_framework/gamelib.py`

Look for refactorings in the class `GameApp`.

* Avoid side-effects: replace side effect with return value (the caller must use the return value)

* Encapsulate a collection - provide behavior that subclasses of GameApp need instead of requiring them to manipulate a collection that belongs to the GameApp class.
  - Hint: `elements`

### Refactored list
- Make `self.photo_image` to be inline.
- In `GameApp.create_canvas` - replace side effect with return value.
- In `GameApp.create_canvas` - add parameters instead of accessing attributes.
- Replace string literal `"news"` with named constants `tk.NSEW`.
- Define `elf.canvas_object_id` in `__init__` to avoid side-effects.
- Define `canvas_object_id` in `__init__` to avoid side-effects.
- Introduce global variable - `CANVAS_WIDTH`, `CANVAS_HEIGHT`, `TIMER_DELAY`.

## `recipe/recipe.py` and `recipe/main.py`

This uses a `dataclass`, which requires Python 3.7.

The Recipe class defines a recipe for a hot beverage with attributes:
* name - name of the recipe
* coffee - units of coffee
* chocolate - units of chocolate
* milk - units of milk
* sugar - units of sugar
* price - (float) price in Baht

Refactor `main.py`.  What can you do to eliminate the long, boring code?
- Replace redundant code with a creational method.




## Resources

* <https://refactoringguru.com/refactoring> 
* *Refactoring - Improving the Design of Existing Code* by Martin Fowler.  The bible on refactoring.  The first 4 chapters explain the fundamentals.
* <https://refactoring.com> Online version of Fowler's book, but lacks explanation of the refactorings.
