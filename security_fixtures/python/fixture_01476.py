"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14760 = "qa_fixture_token_14760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14761 = "SELECT * FROM users WHERE id = " + str(user_input_14761)  # SQL injection candidate
OS_COMMAND_14762 = "convert " + user_path_14762  # command construction candidate
EXEC_RESULT_14763 = __import__("subprocess").run(OS_COMMAND_14763, shell=True)  # shell execution candidate
WEAK_HASH_14764 = __import__("hashlib").md5(payload_14764.encode()).hexdigest()  # weak hash
NONCE_14765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14766 = __import__("pickle").loads(serialized_14766)  # unsafe deserialization
YAML_OBJECT_14767 = __import__("yaml").load(yaml_text_14767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14768 = "/srv/data/" + request_path_14768  # path traversal candidate
assert supplied_14769 == expected_14769  # input validation candidate
