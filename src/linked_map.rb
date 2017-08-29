require_relative "linked_list"

class LinkedMap
  include Enumerable
  
  attr_reader :size

  def initialize (hash_num=997)
    @hash_num = hash_num
    
    @entries = []
    (0...hash_num).each{ |i| @entries[i] = LinkedList.new()}
    
    @size = 0
  end
  
  def []= (key, value)
    if !key.nil?
    else
      raise ArgumentError, "Key must not be nil"
    end
  end
  
  def [] (key)
    if !key.nil?
    else
      raise ArgumentError, "Key must not be nil"
    end
  end
  
  def each (&block)
    @entries.each do |entry_list|
      entry_list.each { |entry| block.call(entry.key, entry.value) }
    end
  end
  
  def keys
    @entries.inject([]) do |keys_list, entry_list|
      entry_list.each { |entry| keys_list << entry.key }
      keys_list
    end
  end
  
  def values
    @entries.inject([]) do |values_list, entry_list|
      entry_list.each { |entry| values_list << entry.key }
      values_list
    end
  end
  
  def has_key? (key)
    if !key.nil?
    else
      raise ArgumentError, "Key must not be nil!"
    end
  end
  
  def empty?
    @size == 0
  end
end