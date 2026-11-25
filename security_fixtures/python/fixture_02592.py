"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25920 = "qa_fixture_token_25920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25921 = "SELECT * FROM users WHERE id = " + str(user_input_25921)  # SQL injection candidate
OS_COMMAND_25922 = "convert " + user_path_25922  # command construction candidate
EXEC_RESULT_25923 = __import__("subprocess").run(OS_COMMAND_25923, shell=True)  # shell execution candidate
WEAK_HASH_25924 = __import__("hashlib").md5(payload_25924.encode()).hexdigest()  # weak hash
NONCE_25925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25926 = __import__("pickle").loads(serialized_25926)  # unsafe deserialization
YAML_OBJECT_25927 = __import__("yaml").load(yaml_text_25927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25928 = "/srv/data/" + request_path_25928  # path traversal candidate
assert supplied_25929 == expected_25929  # input validation candidate
