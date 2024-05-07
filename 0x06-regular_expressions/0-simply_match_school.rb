#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: ruby script_name.rb <string>"
  exit
end

# Get the argument
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /\bSchool\b/

# Perform the regular expression matching
matches = input_string.scan(pattern)

# Print the matches
if matches.empty?
  puts "No matches found."
else
  puts "Matches found: #{matches.join(', ')}"
end
