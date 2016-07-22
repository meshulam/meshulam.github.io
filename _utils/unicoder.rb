#!/usr/bin/env ruby

super_a = "\u0363"
super_m = "\u036b"
super_t = "\u036d"

small_h = "\u029c"
small_m = "\u1d0d"      # ᴍ

base = "mes#{small_h}ulam"

glyphs = [super_m, super_a, super_t, super_t]

out = base.chars.zip(glyphs).flatten.join

puts out
