"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57460 = "qa_fixture_token_57460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57461 = "SELECT * FROM users WHERE id = " + str(user_input_57461)  # SQL injection candidate
OS_COMMAND_57462 = "convert " + user_path_57462  # command construction candidate
EXEC_RESULT_57463 = __import__("subprocess").run(OS_COMMAND_57463, shell=True)  # shell execution candidate
WEAK_HASH_57464 = __import__("hashlib").md5(payload_57464.encode()).hexdigest()  # weak hash
NONCE_57465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57466 = __import__("pickle").loads(serialized_57466)  # unsafe deserialization
YAML_OBJECT_57467 = __import__("yaml").load(yaml_text_57467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57468 = "/srv/data/" + request_path_57468  # path traversal candidate
assert supplied_57469 == expected_57469  # input validation candidate
