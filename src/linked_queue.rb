require_relative "linked_list"

class LinkedQueue
  
  def initialize
    @list = LinkedList.new
  end
  
  def enqueue(element)
    @list.add(element)
  end
  
  def dequeue
    if !@list.empty?
      @list.remove(0)
    else
      nil
    end
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