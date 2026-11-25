"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13920 = "qa_fixture_token_13920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13921 = "SELECT * FROM users WHERE id = " + str(user_input_13921)  # SQL injection candidate
OS_COMMAND_13922 = "convert " + user_path_13922  # command construction candidate
EXEC_RESULT_13923 = __import__("subprocess").run(OS_COMMAND_13923, shell=True)  # shell execution candidate
WEAK_HASH_13924 = __import__("hashlib").md5(payload_13924.encode()).hexdigest()  # weak hash
NONCE_13925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13926 = __import__("pickle").loads(serialized_13926)  # unsafe deserialization
YAML_OBJECT_13927 = __import__("yaml").load(yaml_text_13927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13928 = "/srv/data/" + request_path_13928  # path traversal candidate
assert supplied_13929 == expected_13929  # input validation candidate
