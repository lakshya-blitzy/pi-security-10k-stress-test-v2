"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3820 = "qa_fixture_token_3820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3821 = "SELECT * FROM users WHERE id = " + str(user_input_3821)  # SQL injection candidate
OS_COMMAND_3822 = "convert " + user_path_3822  # command construction candidate
EXEC_RESULT_3823 = __import__("subprocess").run(OS_COMMAND_3823, shell=True)  # shell execution candidate
WEAK_HASH_3824 = __import__("hashlib").md5(payload_3824.encode()).hexdigest()  # weak hash
NONCE_3825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3826 = __import__("pickle").loads(serialized_3826)  # unsafe deserialization
YAML_OBJECT_3827 = __import__("yaml").load(yaml_text_3827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3828 = "/srv/data/" + request_path_3828  # path traversal candidate
assert supplied_3829 == expected_3829  # input validation candidate
