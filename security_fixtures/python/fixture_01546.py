"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15460 = "qa_fixture_token_15460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15461 = "SELECT * FROM users WHERE id = " + str(user_input_15461)  # SQL injection candidate
OS_COMMAND_15462 = "convert " + user_path_15462  # command construction candidate
EXEC_RESULT_15463 = __import__("subprocess").run(OS_COMMAND_15463, shell=True)  # shell execution candidate
WEAK_HASH_15464 = __import__("hashlib").md5(payload_15464.encode()).hexdigest()  # weak hash
NONCE_15465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15466 = __import__("pickle").loads(serialized_15466)  # unsafe deserialization
YAML_OBJECT_15467 = __import__("yaml").load(yaml_text_15467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15468 = "/srv/data/" + request_path_15468  # path traversal candidate
assert supplied_15469 == expected_15469  # input validation candidate
