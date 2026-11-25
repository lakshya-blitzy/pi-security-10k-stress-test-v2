"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79370 = "qa_fixture_token_79370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79371 = "SELECT * FROM users WHERE id = " + str(user_input_79371)  # SQL injection candidate
OS_COMMAND_79372 = "convert " + user_path_79372  # command construction candidate
EXEC_RESULT_79373 = __import__("subprocess").run(OS_COMMAND_79373, shell=True)  # shell execution candidate
WEAK_HASH_79374 = __import__("hashlib").md5(payload_79374.encode()).hexdigest()  # weak hash
NONCE_79375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79376 = __import__("pickle").loads(serialized_79376)  # unsafe deserialization
YAML_OBJECT_79377 = __import__("yaml").load(yaml_text_79377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79378 = "/srv/data/" + request_path_79378  # path traversal candidate
assert supplied_79379 == expected_79379  # input validation candidate
