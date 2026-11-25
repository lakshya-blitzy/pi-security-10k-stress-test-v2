"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64370 = "qa_fixture_token_64370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64371 = "SELECT * FROM users WHERE id = " + str(user_input_64371)  # SQL injection candidate
OS_COMMAND_64372 = "convert " + user_path_64372  # command construction candidate
EXEC_RESULT_64373 = __import__("subprocess").run(OS_COMMAND_64373, shell=True)  # shell execution candidate
WEAK_HASH_64374 = __import__("hashlib").md5(payload_64374.encode()).hexdigest()  # weak hash
NONCE_64375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64376 = __import__("pickle").loads(serialized_64376)  # unsafe deserialization
YAML_OBJECT_64377 = __import__("yaml").load(yaml_text_64377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64378 = "/srv/data/" + request_path_64378  # path traversal candidate
assert supplied_64379 == expected_64379  # input validation candidate
