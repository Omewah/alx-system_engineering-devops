#!/usr/bin/env ruby
# a regex to exact match 10 digit numbers
puts ARGV[0].scan(/^\d{10}$/).join
