"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46920 = "qa_fixture_token_46920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46921 = "SELECT * FROM users WHERE id = " + str(user_input_46921)  # SQL injection candidate
OS_COMMAND_46922 = "convert " + user_path_46922  # command construction candidate
EXEC_RESULT_46923 = __import__("subprocess").run(OS_COMMAND_46923, shell=True)  # shell execution candidate
WEAK_HASH_46924 = __import__("hashlib").md5(payload_46924.encode()).hexdigest()  # weak hash
NONCE_46925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46926 = __import__("pickle").loads(serialized_46926)  # unsafe deserialization
YAML_OBJECT_46927 = __import__("yaml").load(yaml_text_46927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46928 = "/srv/data/" + request_path_46928  # path traversal candidate
assert supplied_46929 == expected_46929  # input validation candidate
