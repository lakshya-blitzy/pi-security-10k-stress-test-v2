"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88760 = "qa_fixture_token_88760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88761 = "SELECT * FROM users WHERE id = " + str(user_input_88761)  # SQL injection candidate
OS_COMMAND_88762 = "convert " + user_path_88762  # command construction candidate
EXEC_RESULT_88763 = __import__("subprocess").run(OS_COMMAND_88763, shell=True)  # shell execution candidate
WEAK_HASH_88764 = __import__("hashlib").md5(payload_88764.encode()).hexdigest()  # weak hash
NONCE_88765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88766 = __import__("pickle").loads(serialized_88766)  # unsafe deserialization
YAML_OBJECT_88767 = __import__("yaml").load(yaml_text_88767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88768 = "/srv/data/" + request_path_88768  # path traversal candidate
assert supplied_88769 == expected_88769  # input validation candidate
