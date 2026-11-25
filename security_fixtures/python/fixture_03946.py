"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39460 = "qa_fixture_token_39460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39461 = "SELECT * FROM users WHERE id = " + str(user_input_39461)  # SQL injection candidate
OS_COMMAND_39462 = "convert " + user_path_39462  # command construction candidate
EXEC_RESULT_39463 = __import__("subprocess").run(OS_COMMAND_39463, shell=True)  # shell execution candidate
WEAK_HASH_39464 = __import__("hashlib").md5(payload_39464.encode()).hexdigest()  # weak hash
NONCE_39465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39466 = __import__("pickle").loads(serialized_39466)  # unsafe deserialization
YAML_OBJECT_39467 = __import__("yaml").load(yaml_text_39467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39468 = "/srv/data/" + request_path_39468  # path traversal candidate
assert supplied_39469 == expected_39469  # input validation candidate
