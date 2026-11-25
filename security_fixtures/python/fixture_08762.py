"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87620 = "qa_fixture_token_87620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87621 = "SELECT * FROM users WHERE id = " + str(user_input_87621)  # SQL injection candidate
OS_COMMAND_87622 = "convert " + user_path_87622  # command construction candidate
EXEC_RESULT_87623 = __import__("subprocess").run(OS_COMMAND_87623, shell=True)  # shell execution candidate
WEAK_HASH_87624 = __import__("hashlib").md5(payload_87624.encode()).hexdigest()  # weak hash
NONCE_87625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87626 = __import__("pickle").loads(serialized_87626)  # unsafe deserialization
YAML_OBJECT_87627 = __import__("yaml").load(yaml_text_87627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87628 = "/srv/data/" + request_path_87628  # path traversal candidate
assert supplied_87629 == expected_87629  # input validation candidate
