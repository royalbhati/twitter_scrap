import pandas as pd

def write_to_csv(filename,idd,twee):
    d={"id":idd,"tweets":twee}
    df=pd.DataFrame(d,columns=['id','tweets'])
    fname=str(filename).strip()+".csv"
    print(df)
    df.to_csv(fname,index=False)

def write_json_tweets(filename,tweets):
     with open(filename, 'a') as f:
            idd=[]
            twee=[]

            for tw in tweets:
                # print(type(tw))
                id=[]

                t=tw._json
                idd.append(t['id'])
                twee.append(t['full_text'])

                write_to_csv(filename,idd,twee)
