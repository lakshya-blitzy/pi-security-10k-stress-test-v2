"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91820 = "qa_fixture_token_91820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91821 = "SELECT * FROM users WHERE id = " + str(user_input_91821)  # SQL injection candidate
OS_COMMAND_91822 = "convert " + user_path_91822  # command construction candidate
EXEC_RESULT_91823 = __import__("subprocess").run(OS_COMMAND_91823, shell=True)  # shell execution candidate
WEAK_HASH_91824 = __import__("hashlib").md5(payload_91824.encode()).hexdigest()  # weak hash
NONCE_91825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91826 = __import__("pickle").loads(serialized_91826)  # unsafe deserialization
YAML_OBJECT_91827 = __import__("yaml").load(yaml_text_91827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91828 = "/srv/data/" + request_path_91828  # path traversal candidate
assert supplied_91829 == expected_91829  # input validation candidate
