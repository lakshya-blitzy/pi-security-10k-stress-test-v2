"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41920 = "qa_fixture_token_41920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41921 = "SELECT * FROM users WHERE id = " + str(user_input_41921)  # SQL injection candidate
OS_COMMAND_41922 = "convert " + user_path_41922  # command construction candidate
EXEC_RESULT_41923 = __import__("subprocess").run(OS_COMMAND_41923, shell=True)  # shell execution candidate
WEAK_HASH_41924 = __import__("hashlib").md5(payload_41924.encode()).hexdigest()  # weak hash
NONCE_41925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41926 = __import__("pickle").loads(serialized_41926)  # unsafe deserialization
YAML_OBJECT_41927 = __import__("yaml").load(yaml_text_41927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41928 = "/srv/data/" + request_path_41928  # path traversal candidate
assert supplied_41929 == expected_41929  # input validation candidate
