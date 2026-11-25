"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37460 = "qa_fixture_token_37460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37461 = "SELECT * FROM users WHERE id = " + str(user_input_37461)  # SQL injection candidate
OS_COMMAND_37462 = "convert " + user_path_37462  # command construction candidate
EXEC_RESULT_37463 = __import__("subprocess").run(OS_COMMAND_37463, shell=True)  # shell execution candidate
WEAK_HASH_37464 = __import__("hashlib").md5(payload_37464.encode()).hexdigest()  # weak hash
NONCE_37465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37466 = __import__("pickle").loads(serialized_37466)  # unsafe deserialization
YAML_OBJECT_37467 = __import__("yaml").load(yaml_text_37467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37468 = "/srv/data/" + request_path_37468  # path traversal candidate
assert supplied_37469 == expected_37469  # input validation candidate
