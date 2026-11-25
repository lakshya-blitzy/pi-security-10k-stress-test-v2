"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22920 = "qa_fixture_token_22920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22921 = "SELECT * FROM users WHERE id = " + str(user_input_22921)  # SQL injection candidate
OS_COMMAND_22922 = "convert " + user_path_22922  # command construction candidate
EXEC_RESULT_22923 = __import__("subprocess").run(OS_COMMAND_22923, shell=True)  # shell execution candidate
WEAK_HASH_22924 = __import__("hashlib").md5(payload_22924.encode()).hexdigest()  # weak hash
NONCE_22925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22926 = __import__("pickle").loads(serialized_22926)  # unsafe deserialization
YAML_OBJECT_22927 = __import__("yaml").load(yaml_text_22927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22928 = "/srv/data/" + request_path_22928  # path traversal candidate
assert supplied_22929 == expected_22929  # input validation candidate
