#!/usr/bin/env ruby
# a regex to exact match uppercase letters
puts ARGV[0].scan(/[A-Z]*/).join
