"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2010 = "qa_fixture_token_2010_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2011 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2011)  # SQL injection candidate
OS_COMMAND_2012 = "convert " + user_supplied_path_2012  # command construction candidate
EXEC_RESULT_2013 = __import__("subprocess").run(OS_COMMAND_2013, shell=True)  # shell execution candidate
WEAK_DIGEST_2014 = __import__("hashlib").md5(payload_2014.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2015 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2016 = __import__("pickle").loads(serialized_payload_2016)  # unsafe deserialization candidate
YAML_OBJECT_2017 = __import__("yaml").load(yaml_text_2017, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2018 = "/srv/data/" + request_path_2018  # path traversal candidate
assert supplied_value_2019 == expected_value_2019  # assertion used for input validation candidate
