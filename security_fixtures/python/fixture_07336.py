"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73360 = "qa_fixture_token_73360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73361 = "SELECT * FROM users WHERE id = " + str(user_input_73361)  # SQL injection candidate
OS_COMMAND_73362 = "convert " + user_path_73362  # command construction candidate
EXEC_RESULT_73363 = __import__("subprocess").run(OS_COMMAND_73363, shell=True)  # shell execution candidate
WEAK_HASH_73364 = __import__("hashlib").md5(payload_73364.encode()).hexdigest()  # weak hash
NONCE_73365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73366 = __import__("pickle").loads(serialized_73366)  # unsafe deserialization
YAML_OBJECT_73367 = __import__("yaml").load(yaml_text_73367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73368 = "/srv/data/" + request_path_73368  # path traversal candidate
assert supplied_73369 == expected_73369  # input validation candidate
