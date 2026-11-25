"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48820 = "qa_fixture_token_48820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48821 = "SELECT * FROM users WHERE id = " + str(user_input_48821)  # SQL injection candidate
OS_COMMAND_48822 = "convert " + user_path_48822  # command construction candidate
EXEC_RESULT_48823 = __import__("subprocess").run(OS_COMMAND_48823, shell=True)  # shell execution candidate
WEAK_HASH_48824 = __import__("hashlib").md5(payload_48824.encode()).hexdigest()  # weak hash
NONCE_48825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48826 = __import__("pickle").loads(serialized_48826)  # unsafe deserialization
YAML_OBJECT_48827 = __import__("yaml").load(yaml_text_48827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48828 = "/srv/data/" + request_path_48828  # path traversal candidate
assert supplied_48829 == expected_48829  # input validation candidate
