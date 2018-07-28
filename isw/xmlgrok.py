'''
Created on Oct 9, 2012

@author: ejamesbe
'''
import xml.dom

def isElementNode(XMLNode):
    return XMLNode.nodeType == xml.dom.Node.ELEMENT_NODE

def firstElementChild(XMLNode):
    ''' Calling firstChild on an Node of type Element often (always?)
    returns a Node of Text type.  How annoying!  Return the first Element
    child
    '''
    child = XMLNode.firstChild
    while child != None and not isElementNode(child):
        child = nextElementSibling(child)
    return child

def nextElementSibling(XMLNode):
    ''' nextElementSibling will return the next sibling of XMLNode that is
    an Element Node Type
    '''
    sib = XMLNode.nextSibling
    while sib != None and not isElementNode(sib):
        sib = sib.nextSibling
    return sib
