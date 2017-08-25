class LinkedList
  include Enumerable
  
  attr_reader :size

  def initialize
    @root_node = nil
    @last_node = nil
    @size = 0
  end
  
  def add(val, index = nil)
    new_node = LinkedList::Node.new(val)
    if index.nil?
      if @root_node.nil?
        @root_node = new_node
        @last_node = @root_node
      else
        @last_node.next_node = new_node
        @last_node = new_node
      end
    else
      if index > -1 and index <= @size
        if index > 0
          before_node = @root_node
          (0...index - 1).each {|i| before_node = before_node.next_node }
          new_node.next_node = before_node.next_node
          before_node.next_node = new_node
          @last_node = new_node if before_node == @last_node
        else
          new_node.next_node = @root_node
          @root_node = new_node
        end
      else
        raise IndexError, "Index #{index} is invalid"
      end
    end
    @size += 1
  end
  
  def remove (index = nil)
    if (index.nil?)
      val = @last_node&.val
      if @root_node == @last_node
        @root_node = nil
      else
        new_current = @root_node.next_node
        while new_current.next_node != @last_node
          new_current = new_current.next_node
        end
        @last_node = new_current
        @last_node.next_node = nil
      end
    else
      if index > -1 and index < @size
        if index > 0
          before_node = @root_node
          (0...index - 1).each {|i| before_node = before_node.next_node }
          @last_node = before_node if before_node.next_node == @last_node
          val = before_node.next_node.val
          before_node.next_node = before_node.next_node&.next_node
        else
          val = @root_node.val
          @root_node = @root_node&.next_node
          @last_node = nil if @root_node.nil?
        end
      else
        raise IndexError, "Index #{index} is invalid"
      end
    end
    @size -= 1
    val
  end
  
  def first
    @root_node.val
  end
  
  def last
    @last_node.val
  end
  
  def join delineator
    ret_str = ""
    current_node = @root_node
    until current_node.nil?
      ret_str << current_node.val&.to_s << delineator
      current_node = current_node.next_node
    end
    ret_str.gsub(/#{Regexp.quote(delineator)}$/, '')
  end

  def each(&block)
    current_node = @root_node
    until current_node.nil?
      block.call(current_node.val)
      current_node = current_node.next_node
    end
  end
  
  def empty?
    @size == 0
  end
  
  def clear
    @root_node = nil
    @last_node = nil
    @size = 0
  end
  
  class Node
    attr_accessor :val
    attr_accessor :next_node

    def initialize(val)
      @val = val
    end
  end
end