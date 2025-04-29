# Stoven

Write a class called `Stoven` (a combined stove and ovent).

- A stoven has 4 burners and an oven.
- Each burner can be individually turned on (`turn_on_burner(index, level)`) or off (`turn_off_burner(index)`), where index is 0–3 and level is 1-10.
- You can call `is_burner_on(index)` to check if a burner is on and it's level.
- The oven can be turned on (`turn_on_oven(temp)`) with a target temperature between 0 and 300 C.
- You can call `turn_off_oven()` to turn it off.
- You can call `oven_status()` which returns "off" or "on at X degrees".
- ... your turn!  Invent 2+ methods for this class.
