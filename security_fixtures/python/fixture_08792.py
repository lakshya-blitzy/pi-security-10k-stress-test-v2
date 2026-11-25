"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87920 = "qa_fixture_token_87920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87921 = "SELECT * FROM users WHERE id = " + str(user_input_87921)  # SQL injection candidate
OS_COMMAND_87922 = "convert " + user_path_87922  # command construction candidate
EXEC_RESULT_87923 = __import__("subprocess").run(OS_COMMAND_87923, shell=True)  # shell execution candidate
WEAK_HASH_87924 = __import__("hashlib").md5(payload_87924.encode()).hexdigest()  # weak hash
NONCE_87925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87926 = __import__("pickle").loads(serialized_87926)  # unsafe deserialization
YAML_OBJECT_87927 = __import__("yaml").load(yaml_text_87927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87928 = "/srv/data/" + request_path_87928  # path traversal candidate
assert supplied_87929 == expected_87929  # input validation candidate
