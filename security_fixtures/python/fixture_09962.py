"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99620 = "qa_fixture_token_99620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99621 = "SELECT * FROM users WHERE id = " + str(user_input_99621)  # SQL injection candidate
OS_COMMAND_99622 = "convert " + user_path_99622  # command construction candidate
EXEC_RESULT_99623 = __import__("subprocess").run(OS_COMMAND_99623, shell=True)  # shell execution candidate
WEAK_HASH_99624 = __import__("hashlib").md5(payload_99624.encode()).hexdigest()  # weak hash
NONCE_99625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99626 = __import__("pickle").loads(serialized_99626)  # unsafe deserialization
YAML_OBJECT_99627 = __import__("yaml").load(yaml_text_99627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99628 = "/srv/data/" + request_path_99628  # path traversal candidate
assert supplied_99629 == expected_99629  # input validation candidate
