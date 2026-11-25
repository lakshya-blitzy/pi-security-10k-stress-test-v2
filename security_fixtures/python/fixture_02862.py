"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28620 = "qa_fixture_token_28620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28621 = "SELECT * FROM users WHERE id = " + str(user_input_28621)  # SQL injection candidate
OS_COMMAND_28622 = "convert " + user_path_28622  # command construction candidate
EXEC_RESULT_28623 = __import__("subprocess").run(OS_COMMAND_28623, shell=True)  # shell execution candidate
WEAK_HASH_28624 = __import__("hashlib").md5(payload_28624.encode()).hexdigest()  # weak hash
NONCE_28625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28626 = __import__("pickle").loads(serialized_28626)  # unsafe deserialization
YAML_OBJECT_28627 = __import__("yaml").load(yaml_text_28627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28628 = "/srv/data/" + request_path_28628  # path traversal candidate
assert supplied_28629 == expected_28629  # input validation candidate
