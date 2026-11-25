"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40920 = "qa_fixture_token_40920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40921 = "SELECT * FROM users WHERE id = " + str(user_input_40921)  # SQL injection candidate
OS_COMMAND_40922 = "convert " + user_path_40922  # command construction candidate
EXEC_RESULT_40923 = __import__("subprocess").run(OS_COMMAND_40923, shell=True)  # shell execution candidate
WEAK_HASH_40924 = __import__("hashlib").md5(payload_40924.encode()).hexdigest()  # weak hash
NONCE_40925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40926 = __import__("pickle").loads(serialized_40926)  # unsafe deserialization
YAML_OBJECT_40927 = __import__("yaml").load(yaml_text_40927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40928 = "/srv/data/" + request_path_40928  # path traversal candidate
assert supplied_40929 == expected_40929  # input validation candidate
