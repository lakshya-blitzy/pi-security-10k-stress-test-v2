"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80760 = "qa_fixture_token_80760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80761 = "SELECT * FROM users WHERE id = " + str(user_input_80761)  # SQL injection candidate
OS_COMMAND_80762 = "convert " + user_path_80762  # command construction candidate
EXEC_RESULT_80763 = __import__("subprocess").run(OS_COMMAND_80763, shell=True)  # shell execution candidate
WEAK_HASH_80764 = __import__("hashlib").md5(payload_80764.encode()).hexdigest()  # weak hash
NONCE_80765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80766 = __import__("pickle").loads(serialized_80766)  # unsafe deserialization
YAML_OBJECT_80767 = __import__("yaml").load(yaml_text_80767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80768 = "/srv/data/" + request_path_80768  # path traversal candidate
assert supplied_80769 == expected_80769  # input validation candidate
