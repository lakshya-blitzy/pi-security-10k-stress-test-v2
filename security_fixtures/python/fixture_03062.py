"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30620 = "qa_fixture_token_30620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30621 = "SELECT * FROM users WHERE id = " + str(user_input_30621)  # SQL injection candidate
OS_COMMAND_30622 = "convert " + user_path_30622  # command construction candidate
EXEC_RESULT_30623 = __import__("subprocess").run(OS_COMMAND_30623, shell=True)  # shell execution candidate
WEAK_HASH_30624 = __import__("hashlib").md5(payload_30624.encode()).hexdigest()  # weak hash
NONCE_30625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30626 = __import__("pickle").loads(serialized_30626)  # unsafe deserialization
YAML_OBJECT_30627 = __import__("yaml").load(yaml_text_30627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30628 = "/srv/data/" + request_path_30628  # path traversal candidate
assert supplied_30629 == expected_30629  # input validation candidate
