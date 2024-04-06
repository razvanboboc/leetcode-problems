// https://leetcode.com/problems/evaluate-reverse-polish-notation/

// You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
// 
// Evaluate the expression. Return an integer that represents the value of the expression.
// 
// Note that:
// 
// The valid operators are '+', '-', '*', and '/'.
// Each operand may be an integer or another expression.
// The division between two integers always truncates toward zero.
// There will not be any division by zero.
// The input represents a valid arithmetic expression in a reverse polish notation.
// The answer and all the intermediate calculations can be represented in a 32-bit integer.

// Sol 1 - O(n) space time complexity. 

public class Solution {
    public int EvalRPN(string[] tokens) {
        Stack<int> stack = new Stack<int>();

        foreach(string token in tokens) {
            if (token == "+") {
                stack.Push(stack.Pop() + stack.Pop());
            } else if(token == "-") {
                int a = stack.Pop();
                int b = stack.Pop();
                stack.Push(b -a);
            } else if(token == "/") {
                int a = stack.Pop();
                int b = stack.Pop();
                stack.Push(b / a);
            } else if(token == "*") {
                stack.Push(stack.Pop() * stack.Pop());
            } else {
                stack.Push(Int32.Parse(token));
            }

        }
        return stack.Pop();
    }
}