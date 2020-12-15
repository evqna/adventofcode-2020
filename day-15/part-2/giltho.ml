let mem = Hashtbl.create 30000000

let max_value = 30000000

let rec loop last_spoken number_spoken =
  if number_spoken = max_value then last_spoken
  else
    let next_spoken =
      match Hashtbl.find_opt mem last_spoken with
      | None -> 0
      | Some v -> number_spoken - v
    in
    Hashtbl.replace mem last_spoken number_spoken;
    loop next_spoken (number_spoken + 1)

let run input =
  let l = String.split_on_char ',' input in
  let number_spoken, last_spoken =
    List.fold_left
      (fun (i, l) n ->
        if i >= 1 then Hashtbl.replace mem l i;
        (i + 1, int_of_string n))
      (0, 0) l
  in
  loop last_spoken number_spoken

let () =
  (* Input is given is Sys.argv.(1) as well as stdin *)
  let input = Sys.argv.(1) in
  let start = Sys.time () *. 1000. in
  let result = run input in
  let end_ = Sys.time () *. 1000. in
  Printf.printf "_duration:%f\n%d\n" (end_ -. start) result
