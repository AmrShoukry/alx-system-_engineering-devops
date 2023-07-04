#!/usr/bin/env ruby
SENDER=ARGV[0].scan(/(?<=\[\bfrom\b:)(\w+|\+?\d+)(?=\])/).join
RECEIVER=ARGV[0].scan(/(?<=\[\bto\b:)(\w+|\+?\d+)(?=\])/).join
FLAGS=ARGV[0].scan(/(?<=\bflags\b:)(?:-?\d+:?)+(?=\])/).join

puts SENDER + "," + RECEIVER + "," + FLAGS
