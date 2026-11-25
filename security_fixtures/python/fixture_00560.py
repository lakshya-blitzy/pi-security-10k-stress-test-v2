"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5600 = "qa_fixture_token_5600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5601 = "SELECT * FROM users WHERE id = " + str(user_input_5601)  # SQL injection candidate
OS_COMMAND_5602 = "convert " + user_path_5602  # command construction candidate
EXEC_RESULT_5603 = __import__("subprocess").run(OS_COMMAND_5603, shell=True)  # shell execution candidate
WEAK_HASH_5604 = __import__("hashlib").md5(payload_5604.encode()).hexdigest()  # weak hash
NONCE_5605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5606 = __import__("pickle").loads(serialized_5606)  # unsafe deserialization
YAML_OBJECT_5607 = __import__("yaml").load(yaml_text_5607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5608 = "/srv/data/" + request_path_5608  # path traversal candidate
assert supplied_5609 == expected_5609  # input validation candidate
