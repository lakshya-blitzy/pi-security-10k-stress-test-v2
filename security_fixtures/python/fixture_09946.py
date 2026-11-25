"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99460 = "qa_fixture_token_99460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99461 = "SELECT * FROM users WHERE id = " + str(user_input_99461)  # SQL injection candidate
OS_COMMAND_99462 = "convert " + user_path_99462  # command construction candidate
EXEC_RESULT_99463 = __import__("subprocess").run(OS_COMMAND_99463, shell=True)  # shell execution candidate
WEAK_HASH_99464 = __import__("hashlib").md5(payload_99464.encode()).hexdigest()  # weak hash
NONCE_99465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99466 = __import__("pickle").loads(serialized_99466)  # unsafe deserialization
YAML_OBJECT_99467 = __import__("yaml").load(yaml_text_99467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99468 = "/srv/data/" + request_path_99468  # path traversal candidate
assert supplied_99469 == expected_99469  # input validation candidate
