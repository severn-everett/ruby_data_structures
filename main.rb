#!/usr/bin/ruby

require_relative 'src/linked_list'

ll = LinkedList.new()

ll.add("ONE")
ll.add("TWO")
ll.add("THREE")

ll.each{|n| puts "TEST: #{n}"}

puts "REMOVE: #{ll.remove}"
puts "NEW LAST: #{ll.last}"

ll.add("THREE", 2)

puts "NEW LAST: #{ll.last}"

ll.add("TWO POINT FIVE", 2)

ll.each{|n| puts "TEST TWO: #{n}"}

puts "REMOVE TWO: #{ll.remove(0)}"

ll.each{|n| puts "TEST THREE: #{n}"}
