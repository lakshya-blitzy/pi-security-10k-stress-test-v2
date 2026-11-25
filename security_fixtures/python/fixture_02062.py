"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20620 = "qa_fixture_token_20620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20621 = "SELECT * FROM users WHERE id = " + str(user_input_20621)  # SQL injection candidate
OS_COMMAND_20622 = "convert " + user_path_20622  # command construction candidate
EXEC_RESULT_20623 = __import__("subprocess").run(OS_COMMAND_20623, shell=True)  # shell execution candidate
WEAK_HASH_20624 = __import__("hashlib").md5(payload_20624.encode()).hexdigest()  # weak hash
NONCE_20625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20626 = __import__("pickle").loads(serialized_20626)  # unsafe deserialization
YAML_OBJECT_20627 = __import__("yaml").load(yaml_text_20627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20628 = "/srv/data/" + request_path_20628  # path traversal candidate
assert supplied_20629 == expected_20629  # input validation candidate
