import artm

def func(text):
    batch_vectorizer = artm.BatchVectorizer(data_path=r'/home/andrew/develop_for_diplom/batch', data_format=text)
    
    model_plsa = artm.ARTM(num_topics=3, scores=[artm.PerplexityScore(name='PerplexityScore', use_unigram_document_model=False, dictionary_name='dictionary')])
    model_plsa.load_dictionary(dictionary_name='dictionary', dictionary_path='/home/andrew/develop_for_diplom/batch/dictionary')
    model_plsa.initialize(dictionary_name='dictionary')
    
    model_plsa.load_dictionary(dictionary_name='dictionary', dictionary_path='/home/andrew/develop_for_diplom/batch/dictionary')
    model_plsa.initialize(dictionary_name='dictionary')
    
    model_plsa.scores.add(artm.SparsityPhiScore(name='SparsityPhiScore'))
    model_plsa.scores.add(artm.SparsityThetaScore(name='SparsityThetaScore'))
    model_plsa.scores.add(artm.TopicKernelScore(name='TopicKernelScore', probability_mass_threshold=0.03))
    
    model_plsa.scores.add(artm.TopTokensScore(name='TopTokensScore', num_tokens=10))
    model_plsa.fit_offline(batch_vectorizer=batch_vectorizer, num_collection_passes=10, num_document_passes=20)
    
    title_1 = '\t\nTOP WORDS OF THE PLSA MODEL:'
    print  title_1
    info.write(str(title_1)+'\n')
    for topic_name in model_plsa.topic_names:
        top_name = str(str(topic_name) + str(': '))
        mod_plsa_scr = model_plsa.score_tracker['TopTokensScore'].last_topic_info[topic_name].tokens
        print top_name,mod_plsa_scr 
        info.write(str(str(top_name)+str(mod_plsa_scr)+'\n'))    
    title_2 = '\nWORDS-TOPIC MATRIX:' 
    print title_2    
    prnt_mod_plsa = model_plsa.phi_
    print prnt_mod_plsa  
    theta_matrix = model_plsa.fit_transform()
    title_3 = '\nTOPIC-DOCUMENTS MATRIX:'
    print title_3
    print theta_matrix,'\n'
    
    
    info.write(str(title_2)+'\n')
    info.write(str(prnt_mod_plsa)+'\n')
    info.write(str(title_3)+'\n')
    info.write(str(theta_matrix)+'\n')
    
    model_plsa.save(filename='/home/andrew/develop_for_diplom/result/plsa_model')    
    
    print_measures(model_plsa)
    
def print_measures(model_plsa):
    print 'Sparsity Phi: {0:.3f} (PLSA)'.format(model_plsa.score_tracker['SparsityPhiScore'].last_value)   
    print 'Sparsity Theta: {0:.3f} (PLSA)'.format(model_plsa.score_tracker['SparsityThetaScore'].last_value)    
    print 'Kernel contrast: {0:.3f} (PLSA)'.format(model_plsa.score_tracker['TopicKernelScore'].last_average_contrast)    
    print 'Kernel purity: {0:.3f} (PLSA)'.format(model_plsa.score_tracker['TopicKernelScore'].last_average_purity)  
    print 'Perplexity: {0:.3f} (PLSA)'.format(model_plsa.score_tracker['PerplexityScore'].last_value)
    
    info.write('\n'+str(str('Sparsity Phi:(PLSA)')+str(format(model_plsa.score_tracker['SparsityPhiScore'].last_value)))+'\n')
    info.write(str(str('Sparsity Theta:(PLSA)')+str(format(model_plsa.score_tracker['SparsityThetaScore'].last_value)))+'\n')
    info.write(str(str('Kernel contrast:(PLSA)')+str(format(model_plsa.score_tracker['TopicKernelScore'].last_average_contrast)))+'\n')
    info.write(str(str('Kernel purity:(PLSA)')+str(format(model_plsa.score_tracker['TopicKernelScore'].last_average_purity)))+'\n')
    info.write(str(str('Perplexity:(PLSA)')+str(format(model_plsa.score_tracker['PerplexityScore'].last_value)))+'\n')

if __name__ == "__main__":
    info = open('/home/andrew/develop_for_diplom/result/info.txt', 'ab')
    text = 'batches'
    func(text)
