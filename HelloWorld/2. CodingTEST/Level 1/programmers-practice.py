class Solution:
    def solutionA(self, character, monsters):
        character = character.split()
        answer = []
        max_value = [-1, -1]
        if int(character[1]) == 0:
            answer.append([0, 0])
        for i in monsters:
            character[0] = 10
            count = 0
            monster = i.split()
            monster[1] = int(monster[1])
            character_attack = int(character[1])
            monster_attack = int(monster[3])
            monster_defense = int(monster[4])
            character_defense = int(character[2])
            character_HP = int(character[0])
            monster_HP = int(monster[2])
            a=0
            if (character_attack - monster_defense) <= 0:
                answer.append([0, 0])
            while (character_attack - monster_defense) > 0:
                monster_HP -= (character_attack - monster_defense)
                count += 1
                if monster_HP <= 0:
                    answer.append([monster[1], monster[1]/count])
                    break
                print("캐릭터의 피sms", character_HP - (monster_attack - character_defense))
                character_HP -= (monster_attack - character_defense)
                print("캐릭터의 피", character[0])
                print("몬스터", monster[0], monster[1], monster[2], monster_attack, monster_defense)
                if character_HP < 0:
                    answer.append([0, 0])
                    break
                else:
                    character_HP = 10
            if max_value[1] < answer[-1][1]:
                max_value = answer[-1]
                max_name = monster[0]
            elif max_value == answer[-1][1]:
                if max_value[0] < answer[-1][0]:
                    max_value = answer[-1]
                    max_name = monster[0]
        return max_name
        return monsters[answer.index(max(answer, key= lambda x: (x[1], x[0])))].split()[0]
a = Solution()
print(a.solutionA("10 5 2", ["Knight 3 10 10 3","Wizard 5 10 15 1","Beginner 1 1 15 1","Beginners 2 1 15 1"]))