require_relative "../src/linked_list"

describe LinkedList do

  describe "#Insertion" do
    before :each do
      @linked_list = LinkedList.new
    end
    
    describe "#Positive" do    
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
        @linked_list.add("FIVE", 4)
        expect(@linked_list.join(", ")).to eql("ONE, TWO, THREE, FOUR, FIVE")
      end
    end
    
    describe "#Negative" do
      it "should not add elements to a negative index" do
        expect{@linked_list.add("NEGATIVE ONE", -1)}.to raise_error(IndexError)
      end
      
      it "should not add elements outside of the index range" do
        @linked_list.add("ONE")
        @linked_list.add("TWO")
        
        expect{@linked_list.add("FIVE", 5)}.to raise_error(IndexError)
      end
    end
  end
  
  describe "#Removal" do
    before :each do
      @linked_list = LinkedList.new
      @linked_list.add("ONE")
      @linked_list.add("TWO")
      @linked_list.add("THREE")
    end
    
    describe "#Positive" do
      it "should remove elements" do
        expect(@linked_list.remove).to eql("THREE")
        expect(@linked_list.join(", ")).to eql("ONE, TWO")
      end
      
      it "should remove elements specified by index" do
        expect(@linked_list.remove(0)).to eql("ONE")
        expect(@linked_list.join(", ")).to eql("TWO, THREE")
      end
      
      it "should be able to clear the list" do
        @linked_list.clear
        expect(@linked_list.size).to be(0)
        expect(@linked_list.empty?).to be(true)
      end
      
      it "should return nothing if removal is done on an empty list" do
        @linked_list.clear
        expect(@linked_list.remove).to be(nil)
      end
    end
    
    describe "#Negative" do
      it "should not remove elements at a negative index" do
        expect{@linked_list.remove(-1)}.to raise_error(IndexError)
      end
      
      it "should not remove elements outside of the index range" do
        expect{@linked_list.remove(5)}.to raise_error(IndexError)
      end
    end
  end
end