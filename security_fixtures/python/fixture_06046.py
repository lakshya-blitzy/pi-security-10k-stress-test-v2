"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60460 = "qa_fixture_token_60460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60461 = "SELECT * FROM users WHERE id = " + str(user_input_60461)  # SQL injection candidate
OS_COMMAND_60462 = "convert " + user_path_60462  # command construction candidate
EXEC_RESULT_60463 = __import__("subprocess").run(OS_COMMAND_60463, shell=True)  # shell execution candidate
WEAK_HASH_60464 = __import__("hashlib").md5(payload_60464.encode()).hexdigest()  # weak hash
NONCE_60465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60466 = __import__("pickle").loads(serialized_60466)  # unsafe deserialization
YAML_OBJECT_60467 = __import__("yaml").load(yaml_text_60467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60468 = "/srv/data/" + request_path_60468  # path traversal candidate
assert supplied_60469 == expected_60469  # input validation candidate
