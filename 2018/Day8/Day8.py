#!/usr/bin/env python3

def ReadFile(FilePath):

   with open(FilePath,'r') as f:
      Lines = f.read().splitlines()

   return(Lines)

def ParseLicense(Line):

   LicenseNumbers = Line.split(" ")

   LicenseNumbers = [ int(LicenseNumber) for LicenseNumber in LicenseNumbers]

   return(LicenseNumbers)


def GetNode(License):

   ChildCount = License[0]
   MetadataCount = License[1]

   Node = {
      "Index": -1,
      "Parent": -1,
      "ChildrenCount": ChildCount,
      "Children": [],
      "ChildrenLength": [],
      "MetadataCount": MetadataCount,
      "MetadataLength": None,
      "TotalLength": None,
   }
   return(Node)

# def GetFirstChild(License):
#    ChildCount = License[0]
#    MetadataCount = License[1]
#    RemainingLicense = License[2:]

#    return(ChildCount, MetadataCount, RemainingLicense)

def GetNextChild(License):
   ChildCount = License[0]
   MetadataCount = License[1]
   RemainingLicense = License[2:]

   return(ChildCount, MetadataCount, RemainingLicense)

def main():

   FilePath = 'D:/OneDrive/Documents/Overig/AdventOfCode/2018/Day8/'
   FileName = 'input.txt'
   # FileName = 'input_test.txt'

   InputFile = FilePath + FileName

   LicenseLines = ReadFile(InputFile)

   License = [ ParseLicense(LicenseLine) for LicenseLine in LicenseLines][0]

   # for Number in License:
   #    print(Number)

   # print( min(License) )

   # Nodes = []

   # Nodes.append( {
   #    "Index": -1,
   #    "Parent": -1,
   #    "Children": [],
   #    "ChildrenLength": [],
   #    "MetadataLength": None,
   #    "TotalLength": None,
   # })

   # print(Nodes)

   Nodes = {}


   # NestCount = 0
   # ChildCount = 1
   # NthChild = 1
   # MetadataCount = 0
   # while len(License) > 0:
   #    # Nodes[ (NestCount, ChildCount) ] = []
   #    print( NestCount, ChildCount )
   #    if NthChild == ChildCount:
   #       Metadata = License[0:MetadataCount]
   #       Nodes[ (NestCount, ChildCount) ] = Metadata
   #       License = License[MetadataCount:]
   #       NthChild = 1
   #       NestCount -= 1
   #    else:
   #       NestCount += 1
   #       NthChild += 1

   #    ChildCount, MetadataCount, License = GetNextChild(License)


   def MakeNode(Index, IndexParent, ChildCount, MetadataCount):
      Node = {
               "Index" : Index,
               "IndexParent" : IndexParent,
               "ChildCount": ChildCount,
               "MetadataCount": MetadataCount,
            }
      return(Node)

   def GetNodeData(Index, License):
      ChildCount = License[Index]
      MetadataCount = License[Index + 1]

      return(ChildCount, MetadataCount)

   def GetChildrenOfNode(Index, Nodes):
      ChildrenIndices = [ NodeIndex for NodeIndex in Nodes if Nodes[NodeIndex]['IndexParent'] == Index ]

      return(ChildrenIndices)

   def GetParentIndex(Node):

      return( Node["IndexParent"] )

   Nodes = {}
   # IndicesOfFirstChildren = []
   # Tree = [[]]
   # NestCount = 0
   ChildCount = 1
   IndexParent = -1
   Index = 0
   # Nodes[-1] = MakeNode(-1, -2, 1, 0)
   while Index < 50000 and Index != -1:
      # IndexParent = Index
      # Index += 2
      # IndicesOfFirstChildren.append(Index)
      # ChildCount = License[Index]
      # MetadataCount = License[Index + 1]
      # CurrentNode = {
      #    "Index" : Index,
      #    "IndexParent" : IndexParent,
      #    "ChildCount": ChildCount,
      #    "MetadataCount": MetadataCount,
      # }
      ChildCount, MetadataCount = GetNodeData(Index, License)
      if Index not in Nodes:
         Nodes[Index] = MakeNode(Index, IndexParent, ChildCount, MetadataCount)
      # IndexParent = Index
      # print( ChildCount, MetadataCount )
      # IndexParent = Index
      # Index += 2
      # NestCount += 1
      # Tree[-1].append( [ (ChildCount, MetadataCount) ] )

      ExistingChildrenOfThisNode = GetChildrenOfNode(Index, Nodes)
      NumberOfChildrenThisNode = len(ExistingChildrenOfThisNode)
      ThisNodeHasMoreChildren = NumberOfChildrenThisNode < Nodes[Index]["ChildCount"]

      # NumberOfChildrenParentNode = len(GetChildrenOfNode(IndexParent, Nodes))
      # ParentNodeHasMoreChildren = NumberOfChildrenParentNode < Nodes[IndexParent]["ChildCount"]

      if ThisNodeHasMoreChildren:
         # print("Finding index of next child of node " + str(Index))
         IndexOfNextChild = Index + 2 + sum( [ Nodes[ChildIndex]["Length"] for ChildIndex in ExistingChildrenOfThisNode] )
         IndexParent = Index
         Index = IndexOfNextChild
      else:
         ThisNodeLength = 2 + sum( [ Nodes[ChildIndex]["Length"] for ChildIndex in ExistingChildrenOfThisNode ] ) + MetadataCount
         Nodes[Index]["Length"] = ThisNodeLength
         Index = Nodes[Index]["IndexParent"]
         # print("All " + str(ChildCount) + " children of node " + str(Index) + " found")
         # print("The children of node " + str(Index) + " are " + str(ExistingChildrenOfThisNode))
         # print("The length of node " + str(Index) + " is " + str(ThisNodeLength) )
         # print( ChildCount, MetadataCount )
         # if Index >= 0:
         #    IndexParent = Nodes[Index]["IndexParent"]

      # if ThisNodeHasMoreChildren:
      #    IndexParent = Index
      # else:
      #    IndexParent = Nodes[Index]["IndexParent"]
         
      # Index += 2

      # print(ThisNodeHasMoreChildren)
      # print(Index)

   # Index += MetadataCount + 2
   # # IndicesOfFirstChildren.append(Index)
   # ChildCount, MetadataCount = GetNodeData(Index, License)
   # # ChildCount = License[Index]
   # # MetadataCount = License[Index + 1]
   # Nodes[Index] = MakeNode(Index, IndexParent, ChildCount, MetadataCount)


   # print( ChildCount, MetadataCount )

   # # print(IndicesOfFirstChildren)
   # print(Tree)

   NodeIndices = [ Key for Key in Nodes ]
   NodeIndices.sort()

   # for NodeIndex in NodeIndices[0:100]:
   #    print(Nodes[NodeIndex])

   AllNodes = [Nodes[NodeIndex] for NodeIndex in NodeIndices]

   NodesWithData = []

   for Node in AllNodes:

      Index = Node["Index"]
      IndexParent = Node["IndexParent"]
      ChildCount = Node["ChildCount"]
      MetadataCount = Node["MetadataCount"]
      Length = Node["Length"]



      Children = GetChildrenOfNode(Index, Nodes)

      MetadatStopIndex = Index + Length
      MetadatStartIndex = MetadatStopIndex - MetadataCount

      Metadata = License[MetadatStartIndex:MetadatStopIndex]

      MetadataCorrectCount = len(Metadata) == MetadataCount
      ChildrenCorrectCount = len(Children) == ChildCount

      if not (MetadataCorrectCount and ChildrenCorrectCount):
         print("Counts are correct: ", MetadataCorrectCount, ChildrenCorrectCount)

      NodeWithData = [Index, IndexParent, ChildCount, Children, MetadatStartIndex, MetadataCount, Metadata]
      NodesWithData.append(NodeWithData)
      # print(Node)

   # AllLengths = [ Node["Length"] for Node in AllNodes] 

   AllMetadata = [NodeWithData[6] for NodeWithData in NodesWithData]

   SummedMetadata = [sum(Metadata) for Metadata in AllMetadata]

   # for Metadata in AllMetadata:
   #    print(Metadata)


   print("The sum of all metadata entries is: ")
   print(sum(SummedMetadata))

   # for NodeWithData in NodesWithData:
   #    print(NodeWithData)


   # NodeValues = {}

   # NodesToCheck = [ NodeWithData for NodeWithData in NodesWithData if NodeWithData[2] == 0]

   # for NodeWithData in NodesToCheck:
   #    Index = NodeWithData[0]
   #    Metadata = NodeWithData[6]
   #    NodeValue = sum(Metadata)
   #    NodeValues[Index] = NodeValue





   # while len(NodeValues) < len(AllNodes):
   #    for NodeWithData in NodesWithData:
   #       Index = NodeWithData[0]
   #       Children = NodeWithData[3]

   #       AllChildrenHaveValues = all( Child in NodeValues for Child in Children )


   #       if AllChildrenHaveValues:
   #          # ChildValues = [(Child, NodeValues[Child]) for Child in Children]
   #          ChildAtPosition = {Children.index(Child) + 1: Child for Child in Children}
   #          ChildValues = {Child: NodeValues[Child] for Child in Children}
   #          Metadata = NodeWithData[6]
   #          Metadata = [ Number for Number in Metadata if Number!= 0 and Number <= len(Children) ]
   #          ThisValue = 0
   #          print(Metadata)
   #          print(ChildAtPosition)
   #          for Number in Metadata:
   #             Child = ChildAtPosition[Number]
   #             print("Child: ", Child)
   #             print(ChildValues)
   #             ThisValue += ChildValues[Child]
   #          print(ThisValue)
   #          NodeValues[Index] = ThisValue 

   # for Node in NodeValues:
   #    print(Node, NodeValues[Node])

   # NodeValues = {}

   # while len(NodeValues) < len(AllNodes):
   #    for NodeWithData in NodesWithData:
   #       Index, IndexParent, ChildCount, Children, MetadatStartIndex, MetadataCount, Metadata = NodeWithData

         
   #       AllChildrenHaveValues = all( Child in NodeValues for Child in Children )


   #       if ChildCount == 0:
   #          ThisNodeValue = sum(Metadata)
   #          NodeValues[Index] = ThisNodeValue
   #       elif AllChildrenHaveValues:
   #          ChildValues = {Child: NodeValues[Child] for Child in Children}
   #          ChildAtPosition = {Children.index(Child) + 1: Child for Child in Children}
   #          ThisNodeValue = sum( [ChildValues[ChildAtPosition[Position]] for Position in Metadata if Position != 0 and Position <= ChildCount] )
   #          print(ChildAtPosition)
   #          print(ChildValues)
   #          print(Metadata)
   #          print(ThisNodeValue)
   #          NodeValues[Index] = ThisNodeValue


   # Nodes = [ Node for Node in NodeValues]
   # Nodes.sort()
   # for Node in Nodes:
   #    print(Node, NodeValues[Node])
      
   # print(NodeValues[0])

   # print( sum(AllLengths) )


   for NodeWithData in NodesWithData:

      Index, IndexParent, ChildCount, Children, MetadatStartIndex, MetadataCount, Metadata = NodeWithData

      # Nodes[Index]

      if ChildCount == 0:
         RelevantMetadata = Metadata
         ChildReferences = []
         Value = sum(RelevantMetadata)
         Nodes[Index]["Value"] = Value
      else:
         RelevantMetadata = [ Number for Number in Metadata if Number != 0 and Number <= ChildCount ]
         Children.sort()
         ChildReferences = [ Children[Number - 1] for Number in RelevantMetadata ]
         # print("Num of children: ", ChildCount)
         # print("RelevantMetadata: ", RelevantMetadata)

      Nodes[Index]["RelevantMetadata"] = RelevantMetadata
      Nodes[Index]["ChildReferences"] = ChildReferences
      Nodes[Index]["Children"] = Children
      Nodes[Index]["Metadata"] = Metadata

   while any( "Value" not in Nodes[Index] for Index in NodeIndices ):
      for Index in NodeIndices:

         if "Value" not in Nodes[Index]:

            ChildReferences = Nodes[Index]["ChildReferences"]
            ChildValues = [ Nodes[ChildIndex]["Value"] for ChildIndex in ChildReferences if "Value" in Nodes[ChildIndex] ]

            # print(Nodes[Index])
            # print(ChildValues)
            # print(ChildReferences)

            if len(ChildValues) == len(ChildReferences):
               Value = sum(ChildValues)
               Nodes[Index]["Value"] = Value

            # print(Nodes[Index])
         
      # print(NodeIndices)

   # for Index in NodeIndices:
   #    print(Nodes[Index])

   RootNodeValue = Nodes[0]["Value"]
   print("What is the value of the root node?")
   print(RootNodeValue)

   return()

if __name__ == "__main__":
   main()