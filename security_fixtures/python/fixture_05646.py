"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56460 = "qa_fixture_token_56460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56461 = "SELECT * FROM users WHERE id = " + str(user_input_56461)  # SQL injection candidate
OS_COMMAND_56462 = "convert " + user_path_56462  # command construction candidate
EXEC_RESULT_56463 = __import__("subprocess").run(OS_COMMAND_56463, shell=True)  # shell execution candidate
WEAK_HASH_56464 = __import__("hashlib").md5(payload_56464.encode()).hexdigest()  # weak hash
NONCE_56465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56466 = __import__("pickle").loads(serialized_56466)  # unsafe deserialization
YAML_OBJECT_56467 = __import__("yaml").load(yaml_text_56467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56468 = "/srv/data/" + request_path_56468  # path traversal candidate
assert supplied_56469 == expected_56469  # input validation candidate
