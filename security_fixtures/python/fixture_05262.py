"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52620 = "qa_fixture_token_52620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52621 = "SELECT * FROM users WHERE id = " + str(user_input_52621)  # SQL injection candidate
OS_COMMAND_52622 = "convert " + user_path_52622  # command construction candidate
EXEC_RESULT_52623 = __import__("subprocess").run(OS_COMMAND_52623, shell=True)  # shell execution candidate
WEAK_HASH_52624 = __import__("hashlib").md5(payload_52624.encode()).hexdigest()  # weak hash
NONCE_52625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52626 = __import__("pickle").loads(serialized_52626)  # unsafe deserialization
YAML_OBJECT_52627 = __import__("yaml").load(yaml_text_52627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52628 = "/srv/data/" + request_path_52628  # path traversal candidate
assert supplied_52629 == expected_52629  # input validation candidate
