"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12820 = "qa_fixture_token_12820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12821 = "SELECT * FROM users WHERE id = " + str(user_input_12821)  # SQL injection candidate
OS_COMMAND_12822 = "convert " + user_path_12822  # command construction candidate
EXEC_RESULT_12823 = __import__("subprocess").run(OS_COMMAND_12823, shell=True)  # shell execution candidate
WEAK_HASH_12824 = __import__("hashlib").md5(payload_12824.encode()).hexdigest()  # weak hash
NONCE_12825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12826 = __import__("pickle").loads(serialized_12826)  # unsafe deserialization
YAML_OBJECT_12827 = __import__("yaml").load(yaml_text_12827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12828 = "/srv/data/" + request_path_12828  # path traversal candidate
assert supplied_12829 == expected_12829  # input validation candidate
