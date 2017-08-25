require_relative "../src/linked_queue"

describe LinkedQueue do

  describe "#Addition" do
    before :each do
      @queue = LinkedQueue.new
    end
  
    it "should queue entries" do
      @queue.enqueue("ONE")
      @queue.enqueue("TWO")
      @queue.enqueue("THREE")
      
      expect(@queue.size).to be(3)
    end
  end
  
  describe "#Removal" do
    before :each do
      @queue = LinkedQueue.new
      @queue.enqueue("ONE")
      @queue.enqueue("TWO")
      @queue.enqueue("THREE")
    end
    
    it "should dequeue entries" do
      expect(@queue.dequeue).to eql("ONE")
      expect(@queue.size).to be(2)
    end
    
    it "should be able to clear its entries" do
      @queue.clear
      expect(@queue.size).to be(0)
      expect(@queue.empty?).to be(true)
    end
    
    it "should do nothing when executing dequeue on an empty queue" do
      @queue.clear
      
      expect(@queue.dequeue).to be(nil)
    end
  end
end