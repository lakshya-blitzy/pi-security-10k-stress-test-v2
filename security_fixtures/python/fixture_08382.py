"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83820 = "qa_fixture_token_83820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83821 = "SELECT * FROM users WHERE id = " + str(user_input_83821)  # SQL injection candidate
OS_COMMAND_83822 = "convert " + user_path_83822  # command construction candidate
EXEC_RESULT_83823 = __import__("subprocess").run(OS_COMMAND_83823, shell=True)  # shell execution candidate
WEAK_HASH_83824 = __import__("hashlib").md5(payload_83824.encode()).hexdigest()  # weak hash
NONCE_83825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83826 = __import__("pickle").loads(serialized_83826)  # unsafe deserialization
YAML_OBJECT_83827 = __import__("yaml").load(yaml_text_83827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83828 = "/srv/data/" + request_path_83828  # path traversal candidate
assert supplied_83829 == expected_83829  # input validation candidate
