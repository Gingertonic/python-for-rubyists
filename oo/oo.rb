class Language
    attr_accessor :name, :in_english
    @@all = []

    def initialize(name, eng_name)
        @name = name
        @in_english = eng_name
        @words = {}
        save
    end

    def save
        @@all << self
    end

    def add_word(english, translation)
        @words[english] = translation
    end

    def how_do_you_say(word)
        puts "In #{name}, '#{word}' is '#{translate(word)}'."
    end

    def self.print_all
        puts "We have the following languages:"
        @@all.each{|lang| puts lang.name}
    end

    private
    def translate(word)
        @words[word]
    end
end

spanish = Language.new("Español", "Spanish")
german = Language.new("Deutsch", "German")

spanish.add_word("Hello", "Hola")
spanish.how_do_you_say("Hello")

Language.print_all