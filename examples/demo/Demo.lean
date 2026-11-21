import Demo.Statement

namespace Demo

private theorem length_step (n : Nat)
    (ih : (List.replicate n true).length = n) :
    (List.replicate (n + 1) true).length = n + 1 := by
  simpa only [List.replicate_succ, List.length_cons] using congrArg Nat.succ ih

theorem result : Target := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih => exact length_step n ih

end Demo
