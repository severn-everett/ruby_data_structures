require_relative "../src/linked_list"

describe LinkedList do

  describe "#Insertion" do
    before :each do
      @linked_list = LinkedList.new
    end
    
    it "should add elements" do
      @linked_list.add("ONE")
      @linked_list.add("TWO")
      @linked_list.add("THREE")
      
      expect(@linked_list.join(", ")).to eql("ONE, TWO, THREE")
      expect(@linked_list.size).to eql(3)
    end
    
    it "should add elements specified by index" do
      @linked_list.add("ONE")
      @linked_list.add("THREE")
      @linked_list.add("FOUR")
      
      @linked_list.add("TWO", 1)
      expect(@linked_list.join(", ")).to eql("ONE, TWO, THREE, FOUR")
    end
  end
end