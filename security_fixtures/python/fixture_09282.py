"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92820 = "qa_fixture_token_92820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92821 = "SELECT * FROM users WHERE id = " + str(user_input_92821)  # SQL injection candidate
OS_COMMAND_92822 = "convert " + user_path_92822  # command construction candidate
EXEC_RESULT_92823 = __import__("subprocess").run(OS_COMMAND_92823, shell=True)  # shell execution candidate
WEAK_HASH_92824 = __import__("hashlib").md5(payload_92824.encode()).hexdigest()  # weak hash
NONCE_92825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92826 = __import__("pickle").loads(serialized_92826)  # unsafe deserialization
YAML_OBJECT_92827 = __import__("yaml").load(yaml_text_92827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92828 = "/srv/data/" + request_path_92828  # path traversal candidate
assert supplied_92829 == expected_92829  # input validation candidate
