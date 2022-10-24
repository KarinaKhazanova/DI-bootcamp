const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }

  for (const key in details) {
    sentence = key + " "+ details[key]
  }

  console.log(sentence)