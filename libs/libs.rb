require 'pry'
require 'httparty'

data = HTTParty.get('https://api.github.com/users/Gingertonic')

binding.pry

puts data["location"]