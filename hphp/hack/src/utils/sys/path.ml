(*
 * Copyright (c) 2015, Facebook, Inc.
 * All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the "hack" directory of this source tree.
 *
 *)

open Hh_prelude
open Reordered_argument_collections
include Stdlib.Sys

module S = struct
  type t = string [@@deriving show]

  let equal = String.equal

  let compare = String.compare

  let to_string x = x
end

type t = S.t [@@deriving show]

let dummy_path : t = ""

let cat = Sys_utils.cat

let equal = S.equal

let compare = S.compare

let dirname = Filename.dirname

let basename = Filename.basename

(**
 * Resolves a path (using realpath)
 *
 * The advantage of using a path instead of strings is that you
 * don't need to care about symlinks or trailing slashes: each
 * path gets normalized by calling realpath.
 *
 * A few things to keep in mind:
 * - paths are always absolute. So the empty string "" becomes
 *   the current directory (in absolute)
 *)
let make path =
  match Sys_utils.realpath path with
  | Some path -> path
  | None -> (* assert false? *) path

(**
 * Creates a Path without running it through `realpath`. This is unsafe because
 * it doesn't normalize symlinks, trailing slashes, or relative paths. The path
 * you pass here must be absolute, and free of symlinks (including ../).
 *)
let make_unsafe path = path

let to_string path = path

(** [concat p1 p2] returns a path equivalent to [p1 ^ "/" ^ p2].
  In the resulting path [p1] (resp. [p2]) has all its trailing (resp. leading) "." and "/" removed.
  eg: concat "a/." ".//b" => "a/b" concat "." "b" => "./b" concat "a" "." => "a/." concat "a" "/b" => "a/b" *)
let concat path more = make (Filename.concat path more)

let parent path =
  if is_directory path then
    make (concat path Filename.parent_dir_name)
  else
    make (Filename.dirname path)

let output = Stdlib.output_string

let slash_escaped_string_of_path path =
  let buf = Buffer.create (String.length path) in
  String.iter
    ~f:(fun ch ->
      match ch with
      | '\\' -> Buffer.add_string buf "zB"
      | ':' -> Buffer.add_string buf "zC"
      | '/' -> Buffer.add_string buf "zS"
      | '\x00' -> Buffer.add_string buf "z0"
      | 'z' -> Buffer.add_string buf "zZ"
      | _ -> Buffer.add_char buf ch)
    path;
  Buffer.contents buf

let path_of_slash_escaped_string str =
  let length = String.length str in
  let buf = Buffer.create length in
  let rec consume i =
    if i >= length then
      ()
    else
      let replacement =
        if i < length - 1 && Char.equal str.[i] 'z' then
          match str.[i + 1] with
          | 'B' -> Some '\\'
          | 'C' -> Some ':'
          | 'S' -> Some '/'
          | '0' -> Some '\x00'
          | 'Z' -> Some 'z'
          | _ -> None
        else
          None
      in
      let (c, next_i) =
        match replacement with
        | Some r -> (r, i + 2)
        | None -> (str.[i], i + 1)
      in
      Buffer.add_char buf c;
      consume next_i
  in
  consume 0;
  make (Buffer.contents buf)

module Set = Reordered_argument_set (Stdlib.Set.Make (S))
