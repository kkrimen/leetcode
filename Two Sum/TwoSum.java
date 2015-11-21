import java.util.HashMap;
import java.util.Map;

public class TwoSum {
	public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] indices = twoSum(nums, target);
        System.out.println(indices[0]);
        System.out.println(indices[1]);
	}

	public static int[] twoSum(int[] nums, int target) {
		Map<Integer, Integer> map = new HashMap<Integer, Integer>(nums.length << 1);
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i]))
                return new int[]{map.get(nums[i]), i + 1};
            else map.put(target - nums[i], i + 1);
        }
        return new int[2];
	}
}