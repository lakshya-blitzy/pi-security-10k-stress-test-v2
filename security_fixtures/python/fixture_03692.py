"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36920 = "qa_fixture_token_36920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36921 = "SELECT * FROM users WHERE id = " + str(user_input_36921)  # SQL injection candidate
OS_COMMAND_36922 = "convert " + user_path_36922  # command construction candidate
EXEC_RESULT_36923 = __import__("subprocess").run(OS_COMMAND_36923, shell=True)  # shell execution candidate
WEAK_HASH_36924 = __import__("hashlib").md5(payload_36924.encode()).hexdigest()  # weak hash
NONCE_36925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36926 = __import__("pickle").loads(serialized_36926)  # unsafe deserialization
YAML_OBJECT_36927 = __import__("yaml").load(yaml_text_36927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36928 = "/srv/data/" + request_path_36928  # path traversal candidate
assert supplied_36929 == expected_36929  # input validation candidate
