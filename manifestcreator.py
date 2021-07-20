#!/usr/bin/env python3
import json

if __name__ == "__main__":
    #Initialization of dictionary to convert into a json later
    manifest = {}
    #Must update file in location to match the most recent run
    linktomanifest = 'https://piranesi-test.reclaim.hosting/with-mirador/media/manifest(2).json'

    #Header
    manifest['@context'] = "http://iiif.io/api/presentation/3/context.json" #Always the same
    manifest['id'] = linktomanifest
    manifest['type'] = 'Manifest'
    manifest['label'] = {'en':['Piranesi Test']}

    #RECOMMENDED Metadata portion
    manifest['metadata'] = []
    manifest['metadata'].append({
        'label': {'en': ['Author']},
        'value': {'none': ['Piranesi']}
    })

    #RECOMMENDED summary
    manifest['summary'] = {'en': ['Pantheon']}

    #RECOMMENDED Thumbnail Note: service not required? not sure what to make id
    manifest['thumbnail'] = []
    manifest['thumbnail'].append({
        'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/page1/full/80,100/0/default.jpg',
        'type': 'Image',
        'format': 'image/jpeg',
        'service': {
            'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/page1',
            'type': 'ImageService3',
            'profile': 'level1'}
    })

    manifest['viewingDirection'] = 'right-to-left'
    manifest['behavior'] = ['paged']
    manifest['navDate'] = '1856-01-01T00:00:00Z' #?

    #MAY have Copyright information
    manifest['rights'] = 'https://creativecommons.org/licenses/by/4.0/'
    manifest['requiredStatement'] = []
    manifest['requiredStatement'].append({
        'label': {'en': ['Attribution']},
        'value': {'en': ['Provided by Internet Archive']}
    })

    #RECOMMENDED Provider
    manifest['provider'] = []
    manifest['provider'].append({
        'id': 'https://sc.edu/about/centers/digital_humanities/projects/digital_piranesi.php',
        'type': 'Agent',
        'label': { 'en': ['Digital Piranesi']},
        'homepage': {
            'id': 'https://sc.edu/about/centers/digital_humanities/projects/digital_piranesi.php',
            'type': 'Test',
            'label': {'en': ['Digital Piranesi Homepage']},
            'format': 'text/html'
        },
        'logo': { #UofSC logo, also change out service for height and width
            'id': 'https://www.thestate.com/latest-news/7yfr5w/picture224247405/alternates/FREE_1140/new%20logo.jpg',
            'type': 'Image',
            'format': 'image/jpeg',
            'height': 100,
            'width': 100
            #'service': {
             #   'id': '',
              #  'type': 'ImageService3',
               # 'profile': 'level2'
            #}
        }
        #'seeAlso': { MAY have
         #   'id': '',
          #  'type': 'Dataset',
           # 'format': 'application/ld+json',
            #'profile': 'https://schema.org'
        #}
    })

    #MAY have a homepage
    #manifest['homepage']= []
    #manifest['homepage'].append({
     #   'id': '',
     #   'type': '',
     #   'label': {'en': ['']},
      #  'format': ''
    #})

    #MAY have a service
    #manifest['service'] = []
    #manifest['service'].append({
     #   'id': '',
      #  'type': '',
       # 'profile': ''
    #})

    #MAY have a seeAlso
    #manifest['seeAlso'] = []
    #manifest['seeAlso'].append({
     #   'id': '',
      #  'type': 'Dataset',
       # 'format': 'text/xml',
        #'profile': ''
    #})

    #MAY have a rendering
    #manifest['rendering'] = []
    #manifest['rendering'].append({
     #   'id': '',
      #  'type': 'Text',
       # 'label': {'en': ['Download as PDF']},
        #'format': 'application/pdf'
    #})

    #MAY have partOf
    #manifest['partOf'] = []
    #manifest['partOf'].append({
     #   'id': '',
      #  'type': 'Collection'
    #})

    #MAY have a start
    #manifest['start'] = []
    #manifest['start'].append({
     #   'id': '',
      #  'type': 'Canvas'
    #})

    #MAY have-logging in instance
    #manifest['services'] = []
    #manifest['services'].append({
     #   '@id': '',
      #  '@type': '',
       # 'profile': '',
        #'label': '',
        #'service': {
         #   '@id': '',
          #  '@type': '',
           # 'profile': ''
        #}
    #})

    #########################################
    #MOST PERTINENT PART-The items listed within Mirador, in this instance only one
    #item exists

    manifest['items'] = []
    manifest['items'].append({
        'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/canvas/p1', #?
        'type': "Canvas",
        'label': {'none': ['p.1']},
        'height': 1000,
        'width': 750,
        'items': {
            'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/page/p1/1',
            'type': 'AnnotationPage',
            'items': {
                'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/annotation/p0001-image',
                'type': 'Annotation',
                'motivation': 'painting',
                'body': {
                    'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/page1/full/max/0/default.jpg',
                    'type': 'Image',
                    'format': 'image/jpeg',
                    'service': {
                        'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/page1',
                        'type': 'ImageService3',
                        'profile': 'level2',
                        'service': {
                            '@id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/auth/login',
                            '@type': 'AuthCookieService1'
                        }
                    },
                    'height': 2000,
                    'width':1500,
                },
                'target': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/canvas/p1'
            },
        },
        'annotations': {
            'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/comments/p1/1',
            'type': 'AnnotationPage'
        }
    })

    #OPTIONAL features

    manifest['structures'] = []
    manifest['structures'].append({
        'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/range/r0',
        'type': 'Range',
        'label': {'en': ['Table of Contents']},
        'items': {
            'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/range/r1',
            'type': 'Range',
            'label': {'en': ['Introduction']},
            'supplementary': {
                'id': '',
                'type': 'AnnotationCollection'
            },
            'items': [{
                'id': '',
                'type': 'Canvas'
            }, {
                'type': 'SpecificResource',
                'source': '',
                'selector': {
                    'type': 'FragmentSelector',
                    'value': 'xywh=0,0,750,300'
                }
            }]
        }
    })
    manifest['annotations'] = []
    manifest['annotations'].append({
        'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/page/manifest/1',
        'type': 'AnnotationPage',
        'items': {
            'id': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/page/manifest/a1',
            'type': 'Annotation',
            'motivation': 'commenting',
            'body': {
                'type': 'TextualBody',
                'language': 'en',
                'value': "I love this manifest!"
            },
            'target': 'https://piranesi-test.reclaim.hosting/with-mirador/media/mymanifesttry3/iiif/book1/manifest'
        }
    })

    #Writes the json file
    with open('manifest.json', 'w') as outfile:
        json.dump(manifest, outfile)