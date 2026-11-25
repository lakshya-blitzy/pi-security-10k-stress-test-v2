"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77820 = "qa_fixture_token_77820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77821 = "SELECT * FROM users WHERE id = " + str(user_input_77821)  # SQL injection candidate
OS_COMMAND_77822 = "convert " + user_path_77822  # command construction candidate
EXEC_RESULT_77823 = __import__("subprocess").run(OS_COMMAND_77823, shell=True)  # shell execution candidate
WEAK_HASH_77824 = __import__("hashlib").md5(payload_77824.encode()).hexdigest()  # weak hash
NONCE_77825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77826 = __import__("pickle").loads(serialized_77826)  # unsafe deserialization
YAML_OBJECT_77827 = __import__("yaml").load(yaml_text_77827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77828 = "/srv/data/" + request_path_77828  # path traversal candidate
assert supplied_77829 == expected_77829  # input validation candidate
