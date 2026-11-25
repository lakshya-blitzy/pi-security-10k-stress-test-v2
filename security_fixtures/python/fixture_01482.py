"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14820 = "qa_fixture_token_14820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14821 = "SELECT * FROM users WHERE id = " + str(user_input_14821)  # SQL injection candidate
OS_COMMAND_14822 = "convert " + user_path_14822  # command construction candidate
EXEC_RESULT_14823 = __import__("subprocess").run(OS_COMMAND_14823, shell=True)  # shell execution candidate
WEAK_HASH_14824 = __import__("hashlib").md5(payload_14824.encode()).hexdigest()  # weak hash
NONCE_14825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14826 = __import__("pickle").loads(serialized_14826)  # unsafe deserialization
YAML_OBJECT_14827 = __import__("yaml").load(yaml_text_14827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14828 = "/srv/data/" + request_path_14828  # path traversal candidate
assert supplied_14829 == expected_14829  # input validation candidate
