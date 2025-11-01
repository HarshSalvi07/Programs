class FileSystem:
    def __init__(self, total_blocks = 20, block_size = 1):
        self.total_blocks = total_blocks
        self.block_size = block_size
        self.free_blocks = [True] * total_blocks  #True = Free, False = Occupied
        self.directory = {}   #{filename:{"size","blocks":[block indices]}}
    
    def allocate_blocks(self, num_blocks):
        """Allocate free blocks for a file"""
        allocated = []
        for i in range(self.total_blocks):
            if self.free_blocks[i]:
                allocated.append(i)
                if len(allocated) ==num_blocks:
                    for blk in allocated:
                        self.free_blocks[blk] = False
                    return allocated
        return None #Not enough space
            
    def create(self,filename,size):
        """Create a file with given size (in blocks)."""
        if filename in self.directory:
            print(f"Error:File'{filename}' already exists")
            return
        
        num_blocks =  (size + self.block_size - 1) //self.block_size
        allocated = self.allocate_blocks(num_blocks)

        if allocated is None:
            print("Error: Not enough space to allocate file")
        else:
            self.directory[filename] = {"size":size, "blocks": allocated}
            print(f"File'{filename}' created with blocks {allocated}")

    def read(self, filename):
        """Read file info."""
        if filename not in self.directory:
            print(f"Error: File ' {filename}'not found")
            return
        file_info = self.directory[filename]
        print(f"Reading file '{filename}':")
        print(f" -> Size:{file_info['size']} units")
        print(f" -> Blocks:{file_info['blocks']}")

    
    def delete(self, filename):
        """Delete a file and free its blocks"""
        if filename not in self.directory:
            print(f"Error:File'{filename}' not found")
            return
        for blk in self.directory[filename]["blocks"]:
            self.free_blocks[blk]  = True
        del self.directory[filename]
        print(f"File' {filename}' deleted successfully")


    def show_directory(self):
        """Show all files and their block allocations"""
        if not self.directory:
            print("Directory is empty")
            return
        print("Directory contents")
        for fname, info in self.directory.items():
            print(f" -> {fname}: size={info['size']}, blocks={info['blocks']}")

    def show_free_blocks(self):
        """Show free/used block status"""
        print("Block allocations status:")
        print("".join(["F" if free else "U" for free in self.free_blocks]))

fs = FileSystem(total_blocks=20,block_size=1)
fs.create('mehta1.txt',3)
fs.create('mehta2.txt',3)
fs.read('mehta1.txt')
fs.read('mehta2.txt')
fs.show_directory()
fs.show_free_blocks()