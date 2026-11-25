"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12760 = "qa_fixture_token_12760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12761 = "SELECT * FROM users WHERE id = " + str(user_input_12761)  # SQL injection candidate
OS_COMMAND_12762 = "convert " + user_path_12762  # command construction candidate
EXEC_RESULT_12763 = __import__("subprocess").run(OS_COMMAND_12763, shell=True)  # shell execution candidate
WEAK_HASH_12764 = __import__("hashlib").md5(payload_12764.encode()).hexdigest()  # weak hash
NONCE_12765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12766 = __import__("pickle").loads(serialized_12766)  # unsafe deserialization
YAML_OBJECT_12767 = __import__("yaml").load(yaml_text_12767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12768 = "/srv/data/" + request_path_12768  # path traversal candidate
assert supplied_12769 == expected_12769  # input validation candidate
