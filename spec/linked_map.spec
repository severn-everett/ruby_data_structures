require_relative "../src/linked_map"

describe LinkedMap do

  describe "#Insertion" do
    before :each do
      @linked_map = LinkedMap.new
    end
    
    describe "#Positive" do
      it "should add elements" do
        @linked_map[:one] = 1
        @linked_map[:two] = 2
        @linked_map[:three] = 3
        
        expect(@linked_map.size).to eql(3)
        expect(@linked_map.keys).to match_array([:one, :two, :three])
        expect(@linked_map.values).to match_array([1, 2, 3])
      end
      
      it "should overwrite values for re-used keys" do
        @linked_map[:one] = 1
        @linked_map[:one] = "UNO"
        
        expect(@linked_map[:one]).to eql("UNO")
      end
    end
    
    describe "#Negative" do
      it "should not add entries with a nil key" do
        nil_key = nil
        expect{@linked_map[nil_key] = "FAIL"}.to raise_error(IndexError)
      end
    end
  end
  
  describe "#Removal" do
    before :each do
      @linked_map = LinkedMap.new
      @linked_map[:one] = 1
      @linked_map[:two] = 2
      @linked_map[:three] = 3
    end
    
    describe "#Positive" do
      it "should remove elements" do
        expect(@linked_map.delete(:two)).to eql(2)
        expect(@linked_map.keys).to match_array([:one, :three])
        expect(@linked_map.values).to match_array([1, 3])
      end
      
      it "should be able to clear the list" do
        @linked_map.clear
        expect(@linked_map.size).to be(0)
        expect(@linked_map.empty?).to be(true)
      end
      
      it "should return nothing if removal is done on an empty list" do
        @linked_map.clear
        expect(@linked_map.delete(:one)).to be(nil)
      end
    end
    
    describe "#Negative" do
      it "should not delete on a nil key" do
        nil_key = nil
        expect{@linked_map.delete(nil_key)}.to raise_error(IndexError)
      end
    end
  end
end