"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88820 = "qa_fixture_token_88820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88821 = "SELECT * FROM users WHERE id = " + str(user_input_88821)  # SQL injection candidate
OS_COMMAND_88822 = "convert " + user_path_88822  # command construction candidate
EXEC_RESULT_88823 = __import__("subprocess").run(OS_COMMAND_88823, shell=True)  # shell execution candidate
WEAK_HASH_88824 = __import__("hashlib").md5(payload_88824.encode()).hexdigest()  # weak hash
NONCE_88825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88826 = __import__("pickle").loads(serialized_88826)  # unsafe deserialization
YAML_OBJECT_88827 = __import__("yaml").load(yaml_text_88827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88828 = "/srv/data/" + request_path_88828  # path traversal candidate
assert supplied_88829 == expected_88829  # input validation candidate
