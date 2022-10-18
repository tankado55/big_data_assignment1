# Context manager

sometimes you have to deal with multiple database connectors (in the data exploration phase, for example), and you’ll have to read from each of them on a regular basis. This might introduce some redundancy, which suggests that a reusable function might be a good fit for this scenario.

# an alternative: decorator