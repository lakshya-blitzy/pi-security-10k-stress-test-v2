"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98920 = "qa_fixture_token_98920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98921 = "SELECT * FROM users WHERE id = " + str(user_input_98921)  # SQL injection candidate
OS_COMMAND_98922 = "convert " + user_path_98922  # command construction candidate
EXEC_RESULT_98923 = __import__("subprocess").run(OS_COMMAND_98923, shell=True)  # shell execution candidate
WEAK_HASH_98924 = __import__("hashlib").md5(payload_98924.encode()).hexdigest()  # weak hash
NONCE_98925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98926 = __import__("pickle").loads(serialized_98926)  # unsafe deserialization
YAML_OBJECT_98927 = __import__("yaml").load(yaml_text_98927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98928 = "/srv/data/" + request_path_98928  # path traversal candidate
assert supplied_98929 == expected_98929  # input validation candidate
