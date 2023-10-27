class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dict = {}
        for path in paths:
            path_parts = path.split()
            directory = path_parts[0]
            files = path_parts[1:]
            for file in files:
                file_parts = file.split('(')
                file_name = file_parts[0]
                content = file_parts[1][:-1]
                file_path = directory + '/' + file_name
                if content in file_dict:
                    file_dict[content].append(file_path)
                else:
                    file_dict[content] = [file_path]
        
        return [file_paths for file_paths in file_dict.values() if len(file_paths) > 1]