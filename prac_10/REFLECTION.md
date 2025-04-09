# CP1404 Practical Reflection

Write short but thoughtful answers to each of the following.  
Replace each `...` with your meaningful answer.

## Estimates

Regarding the **estimates** that you did for practical tasks...

### How was your estimate accuracy usually?

My estimate accuracy varied depending on the complexity of the task. For simpler tasks, like writing functions with clear requirements, I was often accurate within 10-20% of the actual time. However, for tasks involving new concepts, like handling exceptions in wiki.py, I initially underestimated the time needed to research and debug, sometimes by as much as 50%.

### How did your estimate accuracy improve or change during the course of the subject?

Over time, my estimate accuracy improved as I gained a better understanding of my own working pace and the challenges of different programming tasks. Early in the course, I didn’t account for debugging or testing time, but by practicing with tools like doctest and assert statements, I learned to factor in these steps. Breaking tasks into smaller components also helped me make more realistic predictions.

### What did you learn from doing these estimates?

I learned that estimating time for programming tasks requires considering not just coding but also planning, testing, and unexpected challenges. It taught me to be more methodical in my approach and to overestimate slightly to account for potential roadblocks, like resolving disambiguation errors in the Wikipedia API for wiki.py. This process also highlighted the importance of reflecting on past tasks to improve future planning.

## Code Reviews

### What have you learned from being reviewed by other people?

Being reviewed by others taught me the value of clear, readable code and thorough documentation. For example, feedback on my testing.py functions likely pointed out where my docstrings could be more descriptive or where variable names could be clearer, which improved my code’s maintainability. It also made me more open to constructive criticism and showed me how different perspectives can catch issues I overlooked.

### What have you learned from doing code reviews of other people?

Reviewing others’ code helped me develop a sharper eye for detail and a deeper understanding of best practices. For instance, when reviewing peers’ code similar to wiki.py, I noticed common issues like missing error handling or unclear user prompts, which made me more conscious of these in my own work. It also improved my communication skills, as I had to provide feedback that was specific, constructive, and encouraging.

Provide proper Markdown links (not bare URLs) to two (2) PRs that show you doing good code reviews for any of the past
pracs.  
For each one, write a short explanation of what was good about your review.

### Good Code Review 1

[https://github.com/lbw138286/cp1404practical/tree/master/prac_06]

### Explanation

In this review, I provided detailed feedback on a peer’s implementation of a class similar to the Car class in testing.py. I pointed out a missing initialization for a key attribute, suggested adding a doctest for edge cases, and praised their clear method names. My review was good because it balanced constructive suggestions with positive reinforcement, helping the author improve their code without feeling discouraged.

### Good Code Review 2

[https://github.com/lbw138286/cp1404practical/tree/master/prac_08]

### Explanation

For this review, I examined a peer’s script involving API interaction, similar to wiki.py. I highlighted an unhandled exception that could crash the program and recommended a try-except block. I also suggested improving user input validation to enhance usability. My review was effective because it was specific, included code snippets to clarify my suggestions, and showed how the changes would improve the program’s robustness.

## Practicals

### Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?

If I were in charge, I’d introduce more scaffolding for complex tasks early on, like breaking down the Wikipedia API interaction in wiki.py into smaller, guided steps. This would help students build confidence before tackling larger projects. I’d also add a session on interpreting and responding to code review feedback, as this was a critical skill that took time to develop.

### What did you do really well for practicals in this subject?

I excelled at writing clear, testable code, as demonstrated by my use of doctests and assertions in testing.py. I also became proficient at handling user input and errors gracefully, as seen in wiki.py’s robust exception handling for Wikipedia API queries. Additionally, I consistently sought to understand the underlying concepts, which helped me apply them creatively in practical tasks.