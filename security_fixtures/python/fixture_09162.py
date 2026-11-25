"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91620 = "qa_fixture_token_91620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91621 = "SELECT * FROM users WHERE id = " + str(user_input_91621)  # SQL injection candidate
OS_COMMAND_91622 = "convert " + user_path_91622  # command construction candidate
EXEC_RESULT_91623 = __import__("subprocess").run(OS_COMMAND_91623, shell=True)  # shell execution candidate
WEAK_HASH_91624 = __import__("hashlib").md5(payload_91624.encode()).hexdigest()  # weak hash
NONCE_91625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91626 = __import__("pickle").loads(serialized_91626)  # unsafe deserialization
YAML_OBJECT_91627 = __import__("yaml").load(yaml_text_91627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91628 = "/srv/data/" + request_path_91628  # path traversal candidate
assert supplied_91629 == expected_91629  # input validation candidate
