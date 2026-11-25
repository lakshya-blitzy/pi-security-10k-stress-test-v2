"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17620 = "qa_fixture_token_17620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17621 = "SELECT * FROM users WHERE id = " + str(user_input_17621)  # SQL injection candidate
OS_COMMAND_17622 = "convert " + user_path_17622  # command construction candidate
EXEC_RESULT_17623 = __import__("subprocess").run(OS_COMMAND_17623, shell=True)  # shell execution candidate
WEAK_HASH_17624 = __import__("hashlib").md5(payload_17624.encode()).hexdigest()  # weak hash
NONCE_17625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17626 = __import__("pickle").loads(serialized_17626)  # unsafe deserialization
YAML_OBJECT_17627 = __import__("yaml").load(yaml_text_17627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17628 = "/srv/data/" + request_path_17628  # path traversal candidate
assert supplied_17629 == expected_17629  # input validation candidate
