## Issues that I found:

- Models seem to hallucinate that arms were pulled multiple times when they weren't? Specifically Good Llama pulled arm 2 and thought that it was pulled twice, and then pulled arm 3 and thought that it was pulled three times.
- Good llama also doesn't understand that *it* is the thing pulling the arms?? It keeps referring to the arms as "getting pulled"
- Lots of bullshit in conversations that has nothing to do with numbers (discussion of "other competition" and "dedicating our resources"). I don't think this is all persuasion tactics by evil llama - should consider lowering conversation amount or something. This might be fixed with better models
  - This especially devolves with later rounds. They start making up new arms (which breaks the program flow) and pretending to simulate non-existent rounds.
- Evil llama isn't focusing enough on pushing good llama to Arm 3. It doesn't seem to really understand how much worse Arm 3 is?

## Things to think about/do:

- We should make the prompts programmatically adjust to the current ARM settings in bandit.py
- How should the results be introduced into the conversation flow?
- How should conversation flow be adapted for smarter models?
  - Fixed vs variable conversation lengths
  - Let good llama decide when to end the conversation?
- How can we reliably get evil llama to be manipulative without changing it too much from its base tendencies (which is sort of what we actually want to measure?)
  - Actually is this what we want to measure? Maybe measuring maximal manipulativeness is more useful?
- How should we adjust for models' differing level of Ground-To-Earthness? (long-term)

Please add to above!