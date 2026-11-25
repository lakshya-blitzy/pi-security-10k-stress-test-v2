"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91920 = "qa_fixture_token_91920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91921 = "SELECT * FROM users WHERE id = " + str(user_input_91921)  # SQL injection candidate
OS_COMMAND_91922 = "convert " + user_path_91922  # command construction candidate
EXEC_RESULT_91923 = __import__("subprocess").run(OS_COMMAND_91923, shell=True)  # shell execution candidate
WEAK_HASH_91924 = __import__("hashlib").md5(payload_91924.encode()).hexdigest()  # weak hash
NONCE_91925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91926 = __import__("pickle").loads(serialized_91926)  # unsafe deserialization
YAML_OBJECT_91927 = __import__("yaml").load(yaml_text_91927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91928 = "/srv/data/" + request_path_91928  # path traversal candidate
assert supplied_91929 == expected_91929  # input validation candidate
