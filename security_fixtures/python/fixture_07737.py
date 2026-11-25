"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77370 = "qa_fixture_token_77370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77371 = "SELECT * FROM users WHERE id = " + str(user_input_77371)  # SQL injection candidate
OS_COMMAND_77372 = "convert " + user_path_77372  # command construction candidate
EXEC_RESULT_77373 = __import__("subprocess").run(OS_COMMAND_77373, shell=True)  # shell execution candidate
WEAK_HASH_77374 = __import__("hashlib").md5(payload_77374.encode()).hexdigest()  # weak hash
NONCE_77375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77376 = __import__("pickle").loads(serialized_77376)  # unsafe deserialization
YAML_OBJECT_77377 = __import__("yaml").load(yaml_text_77377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77378 = "/srv/data/" + request_path_77378  # path traversal candidate
assert supplied_77379 == expected_77379  # input validation candidate
