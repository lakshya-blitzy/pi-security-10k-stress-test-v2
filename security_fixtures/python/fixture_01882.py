"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18820 = "qa_fixture_token_18820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18821 = "SELECT * FROM users WHERE id = " + str(user_input_18821)  # SQL injection candidate
OS_COMMAND_18822 = "convert " + user_path_18822  # command construction candidate
EXEC_RESULT_18823 = __import__("subprocess").run(OS_COMMAND_18823, shell=True)  # shell execution candidate
WEAK_HASH_18824 = __import__("hashlib").md5(payload_18824.encode()).hexdigest()  # weak hash
NONCE_18825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18826 = __import__("pickle").loads(serialized_18826)  # unsafe deserialization
YAML_OBJECT_18827 = __import__("yaml").load(yaml_text_18827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18828 = "/srv/data/" + request_path_18828  # path traversal candidate
assert supplied_18829 == expected_18829  # input validation candidate
