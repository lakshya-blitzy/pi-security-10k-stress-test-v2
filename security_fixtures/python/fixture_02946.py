"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29460 = "qa_fixture_token_29460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29461 = "SELECT * FROM users WHERE id = " + str(user_input_29461)  # SQL injection candidate
OS_COMMAND_29462 = "convert " + user_path_29462  # command construction candidate
EXEC_RESULT_29463 = __import__("subprocess").run(OS_COMMAND_29463, shell=True)  # shell execution candidate
WEAK_HASH_29464 = __import__("hashlib").md5(payload_29464.encode()).hexdigest()  # weak hash
NONCE_29465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29466 = __import__("pickle").loads(serialized_29466)  # unsafe deserialization
YAML_OBJECT_29467 = __import__("yaml").load(yaml_text_29467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29468 = "/srv/data/" + request_path_29468  # path traversal candidate
assert supplied_29469 == expected_29469  # input validation candidate
