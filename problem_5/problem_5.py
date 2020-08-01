import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if data is None or data == '':
            return
        elif self.head is None:
            self.head = Block(datetime.datetime.utcnow(), data, 0)
            self.tail = self.head
        else:
            self.tail.next = Block(datetime.datetime.utcnow(), data, self.tail.hash)
            self.tail = self.tail.next
        return


    def to_list(self):
        out = []
        block = self.head
        while block:
            out.append(block)
            block = block.next
        return out


def test_function():
    block_chain = BlockChain()
    block_chain.append('hello')
    block_chain.append('hi')
    block_chain.append('blockchain')
    print(block_chain.to_list()) # expect to print block chain

    block_chain2 = BlockChain()
    block_chain2.append(None)
    block_chain2.append(None)
    print(block_chain2.to_list()) # expect to print empty block chain

    block_chain3 = BlockChain()
    block_chain3.append('')
    block_chain3.append('')
    print(block_chain3.to_list()) # expect to print empty block chain

test_function()