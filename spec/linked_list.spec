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
  
  describe "#Access" do
    # The list is not going to be modified during these tests,
    # so we only need to instantiate and populate it once.
    before :all do
      @linked_list = LinkedList.new
      @linked_list.add("ONE")
      @linked_list.add("TWO")
      @linked_list.add("THREE")
    end
    
    describe "#Positive" do
      it "should access elements at a specified index" do
        expect(@linked_list.get(1)).to eql("TWO")
      end
    end
    
    describe "#Negative" do
      it "should not be able to access elements outside of the list's size index" do
        [-1, 5].each do |invalid_index|
          expect{@linked_list.get(invalid_index)}.to raise_error(IndexError)
        end
      end
    end
  end
  
  describe "#Removal" do
    before :each do
      @linked_list = LinkedList.new
      @linked_list.add("ZERO")
      @linked_list.add("ONE")
      @linked_list.add("TWO")
      @linked_list.add("THREE")
    end
    
    describe "#Positive" do
      it "should remove elements" do
        expect(@linked_list.remove).to eql("THREE")
        expect(@linked_list.join(", ")).to eql("ZERO, ONE, TWO")
      end
      
      it "should remove elements specified by index" do
        expect(@linked_list.remove(0)).to eql("ZERO")
        expect(@linked_list.join(", ")).to eql("ONE, TWO, THREE")
      end
      
      it "should remove all elements based on passed-in criteria" do
        @linked_list.delete_if {|x| x.size == 3}
        expect(@linked_list.size).to be(2)
        expect(@linked_list.join(", ")).to eql("ZERO, THREE")
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