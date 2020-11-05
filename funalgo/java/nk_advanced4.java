import java.util.Arrays;
import java.util.TreeMap;
import java.util.stream.IntStream;
import java.util.stream.Stream;

class Main {
    public static int get_longest_subarray_length_of_aim(int[] arr, int aim) {
        int sum = 0;
        int res = Integer.MIN_VALUE;
        var sumMap = new TreeMap<Integer, Integer>();
        sumMap.put(0, -1);
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
            if (sumMap.containsKey(sum - aim)) {
                res = Math.max(i - sumMap.get(sum - aim), res);
            }
            if (!sumMap.containsKey(sum)) {
                sumMap.put(sum, i);
            }
        }
        return res;
    }

    public static int get_longest_subarray_length_which_odd_even_equal(int[] arr, int aim) {
        int[] converted = Arrays.stream(arr).map(x -> x % 2 == 0 ? 1 : -1).toArray();
        return get_longest_subarray_length_of_aim(converted, 0);
    }

    public static void main(String[] args) {
        System.out.println(get_longest_subarray_length_of_aim(
                new int[]{7, 3, 2, 1, 1, 7, -6, -1, 7}, 7));
        System.out.println(get_longest_subarray_length_which_odd_even_equal(
                new int[]{1, 2, 4, 3, 5, 2, 6, 6, 6}, 7));
        System.out.println();
    }
}