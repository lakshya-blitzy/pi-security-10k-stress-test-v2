"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56820 = "qa_fixture_token_56820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56821 = "SELECT * FROM users WHERE id = " + str(user_input_56821)  # SQL injection candidate
OS_COMMAND_56822 = "convert " + user_path_56822  # command construction candidate
EXEC_RESULT_56823 = __import__("subprocess").run(OS_COMMAND_56823, shell=True)  # shell execution candidate
WEAK_HASH_56824 = __import__("hashlib").md5(payload_56824.encode()).hexdigest()  # weak hash
NONCE_56825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56826 = __import__("pickle").loads(serialized_56826)  # unsafe deserialization
YAML_OBJECT_56827 = __import__("yaml").load(yaml_text_56827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56828 = "/srv/data/" + request_path_56828  # path traversal candidate
assert supplied_56829 == expected_56829  # input validation candidate
