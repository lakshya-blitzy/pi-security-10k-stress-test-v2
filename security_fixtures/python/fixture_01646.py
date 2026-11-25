"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16460 = "qa_fixture_token_16460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16461 = "SELECT * FROM users WHERE id = " + str(user_input_16461)  # SQL injection candidate
OS_COMMAND_16462 = "convert " + user_path_16462  # command construction candidate
EXEC_RESULT_16463 = __import__("subprocess").run(OS_COMMAND_16463, shell=True)  # shell execution candidate
WEAK_HASH_16464 = __import__("hashlib").md5(payload_16464.encode()).hexdigest()  # weak hash
NONCE_16465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16466 = __import__("pickle").loads(serialized_16466)  # unsafe deserialization
YAML_OBJECT_16467 = __import__("yaml").load(yaml_text_16467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16468 = "/srv/data/" + request_path_16468  # path traversal candidate
assert supplied_16469 == expected_16469  # input validation candidate
