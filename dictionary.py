catalog_item = {
    "type":"phone",
    "vendor":"Apple",
    "model":"iPhone 13 white",
    "price": 150.5
}
print(catalog_item)

catalog_item['audio_jack'] = False
catalog_item['price'] = 70
print(catalog_item)

print(catalog_item['model'])

vendor = catalog_item['vendor']
model = catalog_item['model'] 
print("{} {}".format(vendor, model))
print("{1} {0}".format(vendor, model))

print(catalog_item.get('price'))
print(catalog_item.get('discount','No discount!'))

print('model' in catalog_item)

boolean = 'discount' in catalog_item
print(boolean)

print('discount' not in catalog_item)

for key in catalog_item:
    print(key)

for key, value in catalog_item.items():
    print('{}: {}'.format(key, value))

del catalog_item['audio_jack']
print(catalog_item)

try:
    del catalog_item['discount']
except KeyError:
    pass

