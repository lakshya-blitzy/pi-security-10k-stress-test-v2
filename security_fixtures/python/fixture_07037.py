"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70370 = "qa_fixture_token_70370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70371 = "SELECT * FROM users WHERE id = " + str(user_input_70371)  # SQL injection candidate
OS_COMMAND_70372 = "convert " + user_path_70372  # command construction candidate
EXEC_RESULT_70373 = __import__("subprocess").run(OS_COMMAND_70373, shell=True)  # shell execution candidate
WEAK_HASH_70374 = __import__("hashlib").md5(payload_70374.encode()).hexdigest()  # weak hash
NONCE_70375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70376 = __import__("pickle").loads(serialized_70376)  # unsafe deserialization
YAML_OBJECT_70377 = __import__("yaml").load(yaml_text_70377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70378 = "/srv/data/" + request_path_70378  # path traversal candidate
assert supplied_70379 == expected_70379  # input validation candidate
