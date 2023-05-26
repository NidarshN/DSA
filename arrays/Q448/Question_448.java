package arrays.Q448;

import java.util.ArrayList;
import java.util.Arrays;
import java.lang.Math;

class Solution{
    public ArrayList<Integer> findDisappearedNumbers(ArrayList<Integer> nums){
        for(int i = 0; i < nums.size(); i++){
            Integer ind = Math.abs(nums.get(i)) - 1;
            Integer val = -1 * Math.abs(nums.get(ind));
            nums.add(i, val);
        }
        ArrayList<Integer> result = new ArrayList<Integer>();
        for(int i=0; i < nums.size();i++){
            if(nums.get(i) > 0){
                result.add(i+1);
            }
        }
        return result;
    }

    public void grader(ArrayList<Integer> answer, ArrayList<Integer> output){
        if(output.equals(answer)){
            System.out.println("Success! \n"+output);
        }else{
            System.out.println("Failure! \n"+output);
        }
    }
}
public class Question_448{
    public static void main(String[] args) {
        Solution solution = new Solution();
        ArrayList<Integer> output1, output2;
        ArrayList<Integer> input1 = new ArrayList<Integer>(Arrays.asList(4,3,2,7,8,2,3,1));
        ArrayList<Integer> input2 = new ArrayList<Integer>(Arrays.asList(5,6));
        ArrayList<Integer> answer1 = new ArrayList<Integer>(Arrays.asList(1, 1));
        ArrayList<Integer> answer2 = new ArrayList<Integer>(Arrays.asList(2));
        output1 = solution.findDisappearedNumbers(input1);
        output2 = solution.findDisappearedNumbers(input2);
        solution.grader(answer1, output1);
        solution.grader(answer2, output2);
    }
}