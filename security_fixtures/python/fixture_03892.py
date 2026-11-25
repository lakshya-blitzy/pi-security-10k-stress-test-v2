"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38920 = "qa_fixture_token_38920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38921 = "SELECT * FROM users WHERE id = " + str(user_input_38921)  # SQL injection candidate
OS_COMMAND_38922 = "convert " + user_path_38922  # command construction candidate
EXEC_RESULT_38923 = __import__("subprocess").run(OS_COMMAND_38923, shell=True)  # shell execution candidate
WEAK_HASH_38924 = __import__("hashlib").md5(payload_38924.encode()).hexdigest()  # weak hash
NONCE_38925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38926 = __import__("pickle").loads(serialized_38926)  # unsafe deserialization
YAML_OBJECT_38927 = __import__("yaml").load(yaml_text_38927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38928 = "/srv/data/" + request_path_38928  # path traversal candidate
assert supplied_38929 == expected_38929  # input validation candidate
