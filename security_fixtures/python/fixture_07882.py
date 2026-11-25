"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78820 = "qa_fixture_token_78820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78821 = "SELECT * FROM users WHERE id = " + str(user_input_78821)  # SQL injection candidate
OS_COMMAND_78822 = "convert " + user_path_78822  # command construction candidate
EXEC_RESULT_78823 = __import__("subprocess").run(OS_COMMAND_78823, shell=True)  # shell execution candidate
WEAK_HASH_78824 = __import__("hashlib").md5(payload_78824.encode()).hexdigest()  # weak hash
NONCE_78825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78826 = __import__("pickle").loads(serialized_78826)  # unsafe deserialization
YAML_OBJECT_78827 = __import__("yaml").load(yaml_text_78827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78828 = "/srv/data/" + request_path_78828  # path traversal candidate
assert supplied_78829 == expected_78829  # input validation candidate
