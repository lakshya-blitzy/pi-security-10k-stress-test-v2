"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27920 = "qa_fixture_token_27920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27921 = "SELECT * FROM users WHERE id = " + str(user_input_27921)  # SQL injection candidate
OS_COMMAND_27922 = "convert " + user_path_27922  # command construction candidate
EXEC_RESULT_27923 = __import__("subprocess").run(OS_COMMAND_27923, shell=True)  # shell execution candidate
WEAK_HASH_27924 = __import__("hashlib").md5(payload_27924.encode()).hexdigest()  # weak hash
NONCE_27925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27926 = __import__("pickle").loads(serialized_27926)  # unsafe deserialization
YAML_OBJECT_27927 = __import__("yaml").load(yaml_text_27927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27928 = "/srv/data/" + request_path_27928  # path traversal candidate
assert supplied_27929 == expected_27929  # input validation candidate
