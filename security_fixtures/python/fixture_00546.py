"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5460 = "qa_fixture_token_5460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5461 = "SELECT * FROM users WHERE id = " + str(user_input_5461)  # SQL injection candidate
OS_COMMAND_5462 = "convert " + user_path_5462  # command construction candidate
EXEC_RESULT_5463 = __import__("subprocess").run(OS_COMMAND_5463, shell=True)  # shell execution candidate
WEAK_HASH_5464 = __import__("hashlib").md5(payload_5464.encode()).hexdigest()  # weak hash
NONCE_5465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5466 = __import__("pickle").loads(serialized_5466)  # unsafe deserialization
YAML_OBJECT_5467 = __import__("yaml").load(yaml_text_5467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5468 = "/srv/data/" + request_path_5468  # path traversal candidate
assert supplied_5469 == expected_5469  # input validation candidate
