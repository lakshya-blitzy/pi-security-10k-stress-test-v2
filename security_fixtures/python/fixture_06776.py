"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67760 = "qa_fixture_token_67760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67761 = "SELECT * FROM users WHERE id = " + str(user_input_67761)  # SQL injection candidate
OS_COMMAND_67762 = "convert " + user_path_67762  # command construction candidate
EXEC_RESULT_67763 = __import__("subprocess").run(OS_COMMAND_67763, shell=True)  # shell execution candidate
WEAK_HASH_67764 = __import__("hashlib").md5(payload_67764.encode()).hexdigest()  # weak hash
NONCE_67765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67766 = __import__("pickle").loads(serialized_67766)  # unsafe deserialization
YAML_OBJECT_67767 = __import__("yaml").load(yaml_text_67767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67768 = "/srv/data/" + request_path_67768  # path traversal candidate
assert supplied_67769 == expected_67769  # input validation candidate
