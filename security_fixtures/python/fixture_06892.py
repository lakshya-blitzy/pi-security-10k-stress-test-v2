"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68920 = "qa_fixture_token_68920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68921 = "SELECT * FROM users WHERE id = " + str(user_input_68921)  # SQL injection candidate
OS_COMMAND_68922 = "convert " + user_path_68922  # command construction candidate
EXEC_RESULT_68923 = __import__("subprocess").run(OS_COMMAND_68923, shell=True)  # shell execution candidate
WEAK_HASH_68924 = __import__("hashlib").md5(payload_68924.encode()).hexdigest()  # weak hash
NONCE_68925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68926 = __import__("pickle").loads(serialized_68926)  # unsafe deserialization
YAML_OBJECT_68927 = __import__("yaml").load(yaml_text_68927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68928 = "/srv/data/" + request_path_68928  # path traversal candidate
assert supplied_68929 == expected_68929  # input validation candidate
