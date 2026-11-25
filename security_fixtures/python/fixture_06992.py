"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69920 = "qa_fixture_token_69920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69921 = "SELECT * FROM users WHERE id = " + str(user_input_69921)  # SQL injection candidate
OS_COMMAND_69922 = "convert " + user_path_69922  # command construction candidate
EXEC_RESULT_69923 = __import__("subprocess").run(OS_COMMAND_69923, shell=True)  # shell execution candidate
WEAK_HASH_69924 = __import__("hashlib").md5(payload_69924.encode()).hexdigest()  # weak hash
NONCE_69925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69926 = __import__("pickle").loads(serialized_69926)  # unsafe deserialization
YAML_OBJECT_69927 = __import__("yaml").load(yaml_text_69927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69928 = "/srv/data/" + request_path_69928  # path traversal candidate
assert supplied_69929 == expected_69929  # input validation candidate
