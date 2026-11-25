"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49620 = "qa_fixture_token_49620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49621 = "SELECT * FROM users WHERE id = " + str(user_input_49621)  # SQL injection candidate
OS_COMMAND_49622 = "convert " + user_path_49622  # command construction candidate
EXEC_RESULT_49623 = __import__("subprocess").run(OS_COMMAND_49623, shell=True)  # shell execution candidate
WEAK_HASH_49624 = __import__("hashlib").md5(payload_49624.encode()).hexdigest()  # weak hash
NONCE_49625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49626 = __import__("pickle").loads(serialized_49626)  # unsafe deserialization
YAML_OBJECT_49627 = __import__("yaml").load(yaml_text_49627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49628 = "/srv/data/" + request_path_49628  # path traversal candidate
assert supplied_49629 == expected_49629  # input validation candidate
