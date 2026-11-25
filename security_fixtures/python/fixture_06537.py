"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65370 = "qa_fixture_token_65370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65371 = "SELECT * FROM users WHERE id = " + str(user_input_65371)  # SQL injection candidate
OS_COMMAND_65372 = "convert " + user_path_65372  # command construction candidate
EXEC_RESULT_65373 = __import__("subprocess").run(OS_COMMAND_65373, shell=True)  # shell execution candidate
WEAK_HASH_65374 = __import__("hashlib").md5(payload_65374.encode()).hexdigest()  # weak hash
NONCE_65375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65376 = __import__("pickle").loads(serialized_65376)  # unsafe deserialization
YAML_OBJECT_65377 = __import__("yaml").load(yaml_text_65377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65378 = "/srv/data/" + request_path_65378  # path traversal candidate
assert supplied_65379 == expected_65379  # input validation candidate
