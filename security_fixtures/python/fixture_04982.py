"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49820 = "qa_fixture_token_49820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49821 = "SELECT * FROM users WHERE id = " + str(user_input_49821)  # SQL injection candidate
OS_COMMAND_49822 = "convert " + user_path_49822  # command construction candidate
EXEC_RESULT_49823 = __import__("subprocess").run(OS_COMMAND_49823, shell=True)  # shell execution candidate
WEAK_HASH_49824 = __import__("hashlib").md5(payload_49824.encode()).hexdigest()  # weak hash
NONCE_49825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49826 = __import__("pickle").loads(serialized_49826)  # unsafe deserialization
YAML_OBJECT_49827 = __import__("yaml").load(yaml_text_49827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49828 = "/srv/data/" + request_path_49828  # path traversal candidate
assert supplied_49829 == expected_49829  # input validation candidate
