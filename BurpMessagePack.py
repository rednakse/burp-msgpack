import json,re,imp
from collections import OrderedDict 
from burp import IBurpExtender
from burp import IMessageEditorTabFactory
from burp import IMessageEditorTab
from burp import IHttpListener

libcode = '''
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
mpNyjdeu1ltbaqi49f+elxcL
'''

libcode = libcode.decode( "base64" ).decode( "zlib" )
msgpack = imp.new_module( "msgpack" )
exec libcode in msgpack.__dict__

class BurpExtender( IBurpExtender, IMessageEditorTabFactory ):
    def registerExtenderCallbacks( self, callbacks ):
        self._callbacks = callbacks
        callbacks.setExtensionName( "Burp MessagePack" )
        callbacks.registerMessageEditorTabFactory( self )
        callbacks.registerHttpListener( HttpListener( callbacks ) )

    def createNewInstance( self, controller, editable ):
        return MessageEditorTab( controller, editable, self._callbacks )

class MpackJsonHelper:
    def __init__( self, callbacks ):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._mpackPattern = re.compile( "^content-type: .*?application/[^;]*?msgpack", re.IGNORECASE )
        self._jsonPattern = re.compile( "[{\[]" )

    def analyzeMessage( self, content, isRequest ):
        if isRequest:
            httpService = self._controller.getHttpService()
            info = self._helpers.analyzeRequest( httpService, content )
        else:
            info = self._helpers.analyzeResponse( content )
        return info

    def isMessagePack( self, headers ):
        for header in headers:
            if None != self._mpackPattern.match( header ):
                return True
        return False

    def buildHttpMessage( self, info, newBody ):
        newRaw = self._helpers.buildHttpMessage( info.getHeaders(), self._helpers.stringToBytes( newBody ))
        return newRaw

    def toJsonBody( self, mpackBody ):
        bodyMap = msgpack.unpackb(mpackBody)
        newBody = json.dumps( bodyMap, ensure_ascii=False, indent=2 ).encode( "utf-8" )
        return newBody

    def toJson( self, raw, info ):
        mpackBody = raw[ info.getBodyOffset() : ].tostring()
        newBody = self.toJsonBody( mpackBody )
        newRaw = self.buildHttpMessage( info, newBody )
        return newRaw

    def toMpackBody( self, body ):
        try:
            jsonBody = json.loads( body, object_pairs_hook=OrderedDict )
            newBody = msgpack.packb( jsonBody )
        except:
            msg = "toMpackBody failure: " + str(body)
            self._callbacks.issueAlert( msg )
            raise Exception( msg )
        return newBody

    def toMpack( self, raw, info ):
        body = raw[ info.getBodyOffset() : ].tostring()
        if None == self._jsonPattern.match( body[0] ):
            return
        newBody = self.toMpackBody( body )
        newRaw = self.buildHttpMessage( info, newBody )
        return newRaw

class MessageEditorTab( IMessageEditorTab, MpackJsonHelper ):
    def __init__( self, controller, editable, callbacks ):
        MpackJsonHelper.__init__( self, callbacks )
        self._controller = controller
        self._editable = editable
        self._editor = self._callbacks.createTextEditor()
        self._editor.setEditable( editable )

    def getTabCaption( self ):
        return "mpack"

    def getUiComponent( self ):
        return self._editor.getComponent()

    def isEnabled( self, content, isRequest ):
        if content is None:
            return False

        info = self.analyzeMessage( content, isRequest )
        isMessagePack = self.isMessagePack( info.getHeaders() )
        return isMessagePack

    def setMessage( self, content, isRequest ):
        info = self.analyzeMessage( content, isRequest )
        newRaw = self.toJson( content, info )
        self._editor.setText( newRaw )
        self._content = content
        self._isRequest = isRequest

    def getMessage( self ):
        content = self._editor.getText()
        info = self.analyzeMessage( content, self._isRequest )
        try:
            newContent = self.toMpack( content, info )
        except:
            return self._content
        return newContent

    def isModified( self ):
        return self._editor.isTextModified()

    def getSelectedData( self ):
        selected = self._editor.getSelectedText()
        return selected

class HttpListener( IHttpListener, MpackJsonHelper ):
    def __init__( self, callbacks ):
        MpackJsonHelper.__init__( self, callbacks )
        self._toolMask = self._callbacks.TOOL_SCANNER | \
            self._callbacks.TOOL_INTRUDER | \
            self._callbacks.TOOL_EXTENDER

    def processHttpMessage( self, toolFlag, isRequest, httpReqRes ):
        if False == isRequest:
            return
        if 0 == ( self._toolMask & toolFlag ):
            return
        requestInfo = self._helpers.analyzeRequest( httpReqRes )
        if False == self._callbacks.isInScope( requestInfo.getUrl() ):
            return
        if False == self.isMessagePack( requestInfo.getHeaders() ):
            return

        rawRequest = httpReqRes.getRequest()
        try:
            newRequest = self.toMpack( rawRequest, requestInfo )
            if None == newRequest:
                return
        except:
            return
        httpReqRes.setRequest( newRequest )
