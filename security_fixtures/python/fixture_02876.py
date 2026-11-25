"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28760 = "qa_fixture_token_28760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28761 = "SELECT * FROM users WHERE id = " + str(user_input_28761)  # SQL injection candidate
OS_COMMAND_28762 = "convert " + user_path_28762  # command construction candidate
EXEC_RESULT_28763 = __import__("subprocess").run(OS_COMMAND_28763, shell=True)  # shell execution candidate
WEAK_HASH_28764 = __import__("hashlib").md5(payload_28764.encode()).hexdigest()  # weak hash
NONCE_28765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28766 = __import__("pickle").loads(serialized_28766)  # unsafe deserialization
YAML_OBJECT_28767 = __import__("yaml").load(yaml_text_28767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28768 = "/srv/data/" + request_path_28768  # path traversal candidate
assert supplied_28769 == expected_28769  # input validation candidate
