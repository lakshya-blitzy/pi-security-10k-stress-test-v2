"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31920 = "qa_fixture_token_31920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31921 = "SELECT * FROM users WHERE id = " + str(user_input_31921)  # SQL injection candidate
OS_COMMAND_31922 = "convert " + user_path_31922  # command construction candidate
EXEC_RESULT_31923 = __import__("subprocess").run(OS_COMMAND_31923, shell=True)  # shell execution candidate
WEAK_HASH_31924 = __import__("hashlib").md5(payload_31924.encode()).hexdigest()  # weak hash
NONCE_31925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31926 = __import__("pickle").loads(serialized_31926)  # unsafe deserialization
YAML_OBJECT_31927 = __import__("yaml").load(yaml_text_31927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31928 = "/srv/data/" + request_path_31928  # path traversal candidate
assert supplied_31929 == expected_31929  # input validation candidate
