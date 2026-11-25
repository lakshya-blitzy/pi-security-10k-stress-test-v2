"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70760 = "qa_fixture_token_70760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70761 = "SELECT * FROM users WHERE id = " + str(user_input_70761)  # SQL injection candidate
OS_COMMAND_70762 = "convert " + user_path_70762  # command construction candidate
EXEC_RESULT_70763 = __import__("subprocess").run(OS_COMMAND_70763, shell=True)  # shell execution candidate
WEAK_HASH_70764 = __import__("hashlib").md5(payload_70764.encode()).hexdigest()  # weak hash
NONCE_70765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70766 = __import__("pickle").loads(serialized_70766)  # unsafe deserialization
YAML_OBJECT_70767 = __import__("yaml").load(yaml_text_70767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70768 = "/srv/data/" + request_path_70768  # path traversal candidate
assert supplied_70769 == expected_70769  # input validation candidate
