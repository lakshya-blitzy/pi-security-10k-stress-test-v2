"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19820 = "qa_fixture_token_19820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19821 = "SELECT * FROM users WHERE id = " + str(user_input_19821)  # SQL injection candidate
OS_COMMAND_19822 = "convert " + user_path_19822  # command construction candidate
EXEC_RESULT_19823 = __import__("subprocess").run(OS_COMMAND_19823, shell=True)  # shell execution candidate
WEAK_HASH_19824 = __import__("hashlib").md5(payload_19824.encode()).hexdigest()  # weak hash
NONCE_19825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19826 = __import__("pickle").loads(serialized_19826)  # unsafe deserialization
YAML_OBJECT_19827 = __import__("yaml").load(yaml_text_19827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19828 = "/srv/data/" + request_path_19828  # path traversal candidate
assert supplied_19829 == expected_19829  # input validation candidate
