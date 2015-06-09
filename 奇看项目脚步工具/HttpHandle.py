import urllib.parse, urllib.request, json,time
import requests
class Request:
    url=''
    method=''
    headers=''
    data=''
    filename=''
    filepath=''
    accessKey=''
    contentType=''
    def RequestGet( self ):
        req = urllib.request.Request(self.url,headers=self.headers,method=self.method)
        response = urllib.request.urlopen(req)
        return response.read().decode('UTF8')
    def RequestPost( self ):
        data =json.dumps(self.data)
        data = data.encode('utf-8')
        req = urllib.request.Request(self.url,data=data,headers=self.headers,method=self.method)
        response = urllib.request.urlopen(req)
        return response.read().decode('UTF8')
    def RequestPostFile( self ):
        files = {'file':(self.filename, open(r''+self.filepath+'','rb'),self.contentType)}
        #boundary = '----------%s' % hex(int(time.time() * 1000))
        #data = []
        #data.append('--%s' % boundary)

        #fr1=open(r''+self.filepath+'','rb')
        #data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('file',self.filename))
        #data.append('Content-Type: %s\r\n' % 'image/jpg')
        #data.append(fr1.read())
        #fr1.close()
        #data.append('--%s--\r\n' % boundary)
    
        #http_body='\r\n'.join(data)
        #req = urllib.request.Request(self.url,data=http_body.encode('utf-8'),method=self.method)
        
        #req.add_header('AccessKey',self.accessKey) 
        #req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
        #response = urllib.request.urlopen(req)
        headers = {'AccessKey': self.accessKey }

    
        response=requests.post(self.url,files=files,headers=headers)
        
        return response.content.decode('UTF8')
    def RequestPostFileWithData( self ):
        files = {'file':(self.filename, open(r''+self.filepath+'','rb'),self.contentType)}
        #boundary = '----------%s' % hex(int(time.time() * 1000))
        #data = []
        #data.append('--%s' % boundary)

        #fr1=open(r''+self.filepath+'','rb')
        #data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('file',self.filename))
        #data.append('Content-Type: %s\r\n' % 'image/jpg')
        #data.append(fr1.read())
        #fr1.close()
        #data.append('--%s--\r\n' % boundary)
    
        #http_body='\r\n'.join(data)
        #req = urllib.request.Request(self.url,data=http_body.encode('utf-8'),method=self.method)
        
        #req.add_header('AccessKey',self.accessKey) 
        #req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
        #response = urllib.request.urlopen(req)
        headers = {'AccessKey': self.accessKey }
        data =self.data
    
        response=requests.post(self.url,data=data,files=files,headers=headers)
        
        return response.content.decode('UTF8')      