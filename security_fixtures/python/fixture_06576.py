"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65760 = "qa_fixture_token_65760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65761 = "SELECT * FROM users WHERE id = " + str(user_input_65761)  # SQL injection candidate
OS_COMMAND_65762 = "convert " + user_path_65762  # command construction candidate
EXEC_RESULT_65763 = __import__("subprocess").run(OS_COMMAND_65763, shell=True)  # shell execution candidate
WEAK_HASH_65764 = __import__("hashlib").md5(payload_65764.encode()).hexdigest()  # weak hash
NONCE_65765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65766 = __import__("pickle").loads(serialized_65766)  # unsafe deserialization
YAML_OBJECT_65767 = __import__("yaml").load(yaml_text_65767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65768 = "/srv/data/" + request_path_65768  # path traversal candidate
assert supplied_65769 == expected_65769  # input validation candidate
