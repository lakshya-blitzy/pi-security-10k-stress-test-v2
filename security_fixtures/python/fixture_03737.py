"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37370 = "qa_fixture_token_37370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37371 = "SELECT * FROM users WHERE id = " + str(user_input_37371)  # SQL injection candidate
OS_COMMAND_37372 = "convert " + user_path_37372  # command construction candidate
EXEC_RESULT_37373 = __import__("subprocess").run(OS_COMMAND_37373, shell=True)  # shell execution candidate
WEAK_HASH_37374 = __import__("hashlib").md5(payload_37374.encode()).hexdigest()  # weak hash
NONCE_37375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37376 = __import__("pickle").loads(serialized_37376)  # unsafe deserialization
YAML_OBJECT_37377 = __import__("yaml").load(yaml_text_37377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37378 = "/srv/data/" + request_path_37378  # path traversal candidate
assert supplied_37379 == expected_37379  # input validation candidate
