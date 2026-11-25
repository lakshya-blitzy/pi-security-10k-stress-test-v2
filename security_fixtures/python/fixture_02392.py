"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23920 = "qa_fixture_token_23920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23921 = "SELECT * FROM users WHERE id = " + str(user_input_23921)  # SQL injection candidate
OS_COMMAND_23922 = "convert " + user_path_23922  # command construction candidate
EXEC_RESULT_23923 = __import__("subprocess").run(OS_COMMAND_23923, shell=True)  # shell execution candidate
WEAK_HASH_23924 = __import__("hashlib").md5(payload_23924.encode()).hexdigest()  # weak hash
NONCE_23925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23926 = __import__("pickle").loads(serialized_23926)  # unsafe deserialization
YAML_OBJECT_23927 = __import__("yaml").load(yaml_text_23927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23928 = "/srv/data/" + request_path_23928  # path traversal candidate
assert supplied_23929 == expected_23929  # input validation candidate
