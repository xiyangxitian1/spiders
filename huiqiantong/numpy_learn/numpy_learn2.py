import numpy as np
import random

"""
猜奖问题  有3个门，只有一个门后有奖，你选择了一个后，会打开一个空门，
问你是否更换你选择的。
是换中奖的概率高，还是不换中奖的概率高呢。
"""


def gen_random(num=100):
    # 奖品在1，2，3号门中随机出现
    lst = np.random.randint(1, 4, size=num)
    return lst


# print(gen_random())


# 定义基于第一种猜法的函数(不换)
def guess_one(num=100):
    # 生成正确的答案
    lst = gen_random(num)
    # 猜的轮数和前面生成的轮数一致，这里默认玩100次，
    # （生成100次正确答案，对应猜100次）
    guess = np.random.randint(1, 4, size=len(lst))
    # 计算有多少个正确的，相等即为正确，最终返回False和True的序列
    judge = (lst == guess)
    # 因为True默认是1，False默认是0，我们直接求和，来计算正确率是多少
    correct_rate = judge.sum() / len(judge)
    print('Bro,这次我们玩%d轮~' % num)
    print('在第二次不改变选择的策略下，你最终的中奖率是:%.2f' % (correct_rate * 100))


# 定义基于第2种猜法的函数(换)
def guess_two(num=100):
    # 生成100次正确答案
    lst = gen_random(num)
    # 第一步，依然是随机猜100次
    guess = np.random.randint(1, 4, size=len(lst))
    # 因为第二次我们会改变选择，这里创建一个列表来存储我们改变后的最终选择
    guess_change = []

    for anwser, g in zip(lst, guess):
        # 无论是否中奖，在主持人第一次打开门阶段，我们选择的门不会被打开，
        # 背后是大奖的门也不会被打开（有时候可能是同一个）
        # 举个例子：当我们选择的是A门，大奖藏在B门，那主持人帮我们打开的空门一定是C门，然后
        # 问我们是否改变选择，也就是说，当我们第一步猜的和正确答案不一致，
        # 改变选择之后我们一定会中奖

        # answer是正确答案，g是我们第一步猜的
        if anwser != g:
            # 如果正确答案和我们第一次猜的不一致，主持人排除掉一个门后
            # 我们改变选择，肯定选的是正确答案
            guess_change.append(anwser)
        else:
            # 当我们猜的门和正确答案一致，主持人随机打开一遍门之后，我们会
            # 选择剩下的一扇未被打开的门
            # 继续举个例子，如果我们选择的是A门，大奖就在A门，那么真理既然被我们
            # 选中，主持人在没有奖的B和C门中随机打开一扇都可以
            # 然后问我们是否change，要是B门被打开，那么剩下A（我们第一步选择的）
            # 和C门，我们会改变立场去选择C门，结果就是大奖飞走了

            anwser_range = [1, 2, 3]
            # 我们选择的就是正确答案，先排除掉（因为最后我们会改变选择）
            anwser_range.remove(anwser)
            # 主持人随机打开一个门
            anwser_range.remove(anwser_range[random.randint(0, 1)])
            # 剩下的就是我们最终选择的门
            guess_change.append(anwser_range[0])

    # 到这一步，我们对刚才改变选择之后的结果进行汇总
    guess_change = np.array(guess_change)
    # 看看猜对了多少轮
    judge = (lst == guess_change)
    # 正确率是多少
    correct_rate = judge.sum() / len(judge)
    print('Bro,这次我们玩%d轮~' % num)
    print('在第二次改变选择的策略下，你最终的中奖率是:%.2f' % (correct_rate * 100))

for i in range(10):
    guess_one()
print("********************************")
for i in range(10):
    guess_two()
