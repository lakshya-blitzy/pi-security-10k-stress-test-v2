"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21460 = "qa_fixture_token_21460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21461 = "SELECT * FROM users WHERE id = " + str(user_input_21461)  # SQL injection candidate
OS_COMMAND_21462 = "convert " + user_path_21462  # command construction candidate
EXEC_RESULT_21463 = __import__("subprocess").run(OS_COMMAND_21463, shell=True)  # shell execution candidate
WEAK_HASH_21464 = __import__("hashlib").md5(payload_21464.encode()).hexdigest()  # weak hash
NONCE_21465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21466 = __import__("pickle").loads(serialized_21466)  # unsafe deserialization
YAML_OBJECT_21467 = __import__("yaml").load(yaml_text_21467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21468 = "/srv/data/" + request_path_21468  # path traversal candidate
assert supplied_21469 == expected_21469  # input validation candidate
