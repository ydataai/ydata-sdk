"""
    Validate and process the payload for the synthesizers anonymizer
"""

from ydata.datascience.common import AnonymizerType

def build_and_validate_anonimization(anonimyze:dict, cols: list) -> dict:
    isnested = any(isinstance(i,dict) for i in anonimyze.values())

    if not all([True if k in cols else False for k in list(anonimyze.keys())]):
        #AnonymizationConfigurationError
        raise Exception('The keys in your configuration must exactly match the column names in the provided dataset. Please check and update your inputs to ensure they align.')

    if isnested:
        # Validate the format here.
        for k, v in anonimyze.items():
            if 'type' not in list(v.keys()):
                raise Exception("""The provided configuration is not correct. Make sure that your anonymization config follow one of the following formats:

                                {
                                    'col_name': {'type': 'anonymization_method', kwargs**}

                                } or

                                {
                                    'col_name: 'anonymization_method'
                                }
                                """)
            else:
                anon_type = anonimyze[k]['type']
                anonimyze[k]['type'] = AnonymizerType.get_anonymizer_type(anon_type).value
        config = anonimyze
    else:
        config = {}
        for k,v in anonimyze.items():
            print(k,v)
            if AnonymizerType.get_anonymizer_type(v) is None:
                col_config = {'type': AnonymizerType.REGEX.value, 'regex': v}
            else:
                col_config = {'type': AnonymizerType.get_anonymizer_type(v).value}

            config[k] = col_config

    return config
