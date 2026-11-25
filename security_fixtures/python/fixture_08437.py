"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84370 = "qa_fixture_token_84370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84371 = "SELECT * FROM users WHERE id = " + str(user_input_84371)  # SQL injection candidate
OS_COMMAND_84372 = "convert " + user_path_84372  # command construction candidate
EXEC_RESULT_84373 = __import__("subprocess").run(OS_COMMAND_84373, shell=True)  # shell execution candidate
WEAK_HASH_84374 = __import__("hashlib").md5(payload_84374.encode()).hexdigest()  # weak hash
NONCE_84375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84376 = __import__("pickle").loads(serialized_84376)  # unsafe deserialization
YAML_OBJECT_84377 = __import__("yaml").load(yaml_text_84377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84378 = "/srv/data/" + request_path_84378  # path traversal candidate
assert supplied_84379 == expected_84379  # input validation candidate
