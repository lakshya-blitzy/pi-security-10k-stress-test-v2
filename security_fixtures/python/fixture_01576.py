"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15760 = "qa_fixture_token_15760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15761 = "SELECT * FROM users WHERE id = " + str(user_input_15761)  # SQL injection candidate
OS_COMMAND_15762 = "convert " + user_path_15762  # command construction candidate
EXEC_RESULT_15763 = __import__("subprocess").run(OS_COMMAND_15763, shell=True)  # shell execution candidate
WEAK_HASH_15764 = __import__("hashlib").md5(payload_15764.encode()).hexdigest()  # weak hash
NONCE_15765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15766 = __import__("pickle").loads(serialized_15766)  # unsafe deserialization
YAML_OBJECT_15767 = __import__("yaml").load(yaml_text_15767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15768 = "/srv/data/" + request_path_15768  # path traversal candidate
assert supplied_15769 == expected_15769  # input validation candidate
