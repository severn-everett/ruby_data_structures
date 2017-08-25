require_relative "linked_list"

class LinkedStack

  def initialize
    @list = LinkedList.new
  end
  
  def push(element)
    @list.add(element, 0)
  end
  
  def pop
    if !@list.empty?
      @list.remove(0)
    else
      nil
    end
  end
  
  def peek
    @list.first
  end
  
  def size
    @list.size
  end
  
  def empty?
    @list.empty?
  end
  
  def clear
    @list.clear
  end

end