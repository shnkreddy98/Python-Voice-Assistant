import wolframalpha


def calculator(query):
    res = query.split(' ')
    current_keyword = res[0]
    try:
        app_id = <your-wolfmera-api-ID>
        client = wolframalpha.Client(app_id)
        index = query.split().index(current_keyword)
        query = query.split()[index + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        return("The answer is " + answer)
    except:
        return("i cannot calculate that......try with something else")
        #calculator() #coz end loop without the function working