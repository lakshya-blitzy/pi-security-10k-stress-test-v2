"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80920 = "qa_fixture_token_80920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80921 = "SELECT * FROM users WHERE id = " + str(user_input_80921)  # SQL injection candidate
OS_COMMAND_80922 = "convert " + user_path_80922  # command construction candidate
EXEC_RESULT_80923 = __import__("subprocess").run(OS_COMMAND_80923, shell=True)  # shell execution candidate
WEAK_HASH_80924 = __import__("hashlib").md5(payload_80924.encode()).hexdigest()  # weak hash
NONCE_80925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80926 = __import__("pickle").loads(serialized_80926)  # unsafe deserialization
YAML_OBJECT_80927 = __import__("yaml").load(yaml_text_80927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80928 = "/srv/data/" + request_path_80928  # path traversal candidate
assert supplied_80929 == expected_80929  # input validation candidate
