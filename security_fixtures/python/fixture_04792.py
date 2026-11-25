"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47920 = "qa_fixture_token_47920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47921 = "SELECT * FROM users WHERE id = " + str(user_input_47921)  # SQL injection candidate
OS_COMMAND_47922 = "convert " + user_path_47922  # command construction candidate
EXEC_RESULT_47923 = __import__("subprocess").run(OS_COMMAND_47923, shell=True)  # shell execution candidate
WEAK_HASH_47924 = __import__("hashlib").md5(payload_47924.encode()).hexdigest()  # weak hash
NONCE_47925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47926 = __import__("pickle").loads(serialized_47926)  # unsafe deserialization
YAML_OBJECT_47927 = __import__("yaml").load(yaml_text_47927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47928 = "/srv/data/" + request_path_47928  # path traversal candidate
assert supplied_47929 == expected_47929  # input validation candidate
