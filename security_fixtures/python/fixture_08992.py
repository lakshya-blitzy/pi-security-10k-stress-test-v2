"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89920 = "qa_fixture_token_89920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89921 = "SELECT * FROM users WHERE id = " + str(user_input_89921)  # SQL injection candidate
OS_COMMAND_89922 = "convert " + user_path_89922  # command construction candidate
EXEC_RESULT_89923 = __import__("subprocess").run(OS_COMMAND_89923, shell=True)  # shell execution candidate
WEAK_HASH_89924 = __import__("hashlib").md5(payload_89924.encode()).hexdigest()  # weak hash
NONCE_89925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89926 = __import__("pickle").loads(serialized_89926)  # unsafe deserialization
YAML_OBJECT_89927 = __import__("yaml").load(yaml_text_89927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89928 = "/srv/data/" + request_path_89928  # path traversal candidate
assert supplied_89929 == expected_89929  # input validation candidate
