"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16370 = "qa_fixture_token_16370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16371 = "SELECT * FROM users WHERE id = " + str(user_input_16371)  # SQL injection candidate
OS_COMMAND_16372 = "convert " + user_path_16372  # command construction candidate
EXEC_RESULT_16373 = __import__("subprocess").run(OS_COMMAND_16373, shell=True)  # shell execution candidate
WEAK_HASH_16374 = __import__("hashlib").md5(payload_16374.encode()).hexdigest()  # weak hash
NONCE_16375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16376 = __import__("pickle").loads(serialized_16376)  # unsafe deserialization
YAML_OBJECT_16377 = __import__("yaml").load(yaml_text_16377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16378 = "/srv/data/" + request_path_16378  # path traversal candidate
assert supplied_16379 == expected_16379  # input validation candidate
