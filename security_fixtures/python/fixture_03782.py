"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37820 = "qa_fixture_token_37820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37821 = "SELECT * FROM users WHERE id = " + str(user_input_37821)  # SQL injection candidate
OS_COMMAND_37822 = "convert " + user_path_37822  # command construction candidate
EXEC_RESULT_37823 = __import__("subprocess").run(OS_COMMAND_37823, shell=True)  # shell execution candidate
WEAK_HASH_37824 = __import__("hashlib").md5(payload_37824.encode()).hexdigest()  # weak hash
NONCE_37825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37826 = __import__("pickle").loads(serialized_37826)  # unsafe deserialization
YAML_OBJECT_37827 = __import__("yaml").load(yaml_text_37827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37828 = "/srv/data/" + request_path_37828  # path traversal candidate
assert supplied_37829 == expected_37829  # input validation candidate
