require_relative "../src/linked_stack"

describe LinkedStack do

  describe "#Addition" do
    before :each do
      @stack = LinkedStack.new
    end
  
    it "should push entries" do
      @stack.push("ONE")
      @stack.push("TWO")
      @stack.push("THREE")
      
      expect(@stack.size).to be(3)
      expect(@stack.peek).to eql("THREE")
    end
  end
  
  describe "#Removal" do
    before :each do
      @stack = LinkedStack.new
      @stack.push("ONE")
      @stack.push("TWO")
      @stack.push("THREE")
    end
    
    it "should pop entries" do
      expect(@stack.pop).to eql("THREE")
      expect(@stack.size).to be(2)
    end
    
    it "should be able to clear its entries" do
      @stack.clear
      expect(@stack.size).to be(0)
      expect(@stack.empty?).to be(true)
    end
    
    it "should do nothing when executing pop on an empty stack" do
      @stack.clear
      
      expect(@stack.pop).to be(nil)
    end
  end
end