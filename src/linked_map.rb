require_relative "linked_list"

class LinkedMap
  include Enumerable
  
  EntryPair = Struct.new(:key, :value)
  
  attr_reader :size

  def initialize (hash_num=997)
    @hash_num = hash_num
    
    @entries = []
    (0...hash_num).each{ |i| @entries[i] = LinkedList.new()}
    
    @size = 0
  end
  
  def []= (key, value)
    entry_list = get_entry_list(key)
    entry_pair = entry_list.find{|ep| ep.key.eql?(key)}
    if entry_pair.nil?
      entry_list.add(EntryPair.new(key, value))
    else
      entry_pair.value = value
    end
    @size += 1
  end
  
  def [] (key)
    get_entry_list(key).find{|ep| ep.key.eql?(key)}&.value
  end
  
  def delete (key)
    if !empty?
      entry_list = get_entry_list(key)
      entry_index = entry_list.find_index{|ep| ep.key.eql?(key)}
      @size -= 1
      entry_list.remove(entry_index).value
    else
      nil
    end
  end
  
  def delete_if (&block)
    @entries.each do |entry_list|
      current_node = entry_list.instance_variable_get(:@root_node)
      previous_node = nil
      while (!current_node.nil?) do
        next_node = current_node.next_node
        if block.call(current_node.val.key, current_node.val.value)
          if previous_node.nil? # Removing the root node
            entry_list.remove(0)
          else # Removing a non-root node manually
            previous_node.next_node = current_node.next_node
            @size -= 1
          end
        else # No deletion - set up previous node to be current node
          previous_node = current_node
        end
        current_node = next_node
      end
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
      entry_list.each { |entry| values_list << entry.value }
      values_list
    end
  end
  
  def has_key? (key)
    get_entry_list(key).find{|ep| ep.key.any?(key)}
  end
  
  def empty?
    @size == 0
  end
  
  def clear
    @entries.each(&:clear)
    @size = 0
  end
  
  private
  def get_entry_list (key)
    if !key.nil?
      @entries[key.hash.abs % @hash_num]
    else
      raise IndexError, "Key must not be nil!"
    end
  end
end