"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34920 = "qa_fixture_token_34920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34921 = "SELECT * FROM users WHERE id = " + str(user_input_34921)  # SQL injection candidate
OS_COMMAND_34922 = "convert " + user_path_34922  # command construction candidate
EXEC_RESULT_34923 = __import__("subprocess").run(OS_COMMAND_34923, shell=True)  # shell execution candidate
WEAK_HASH_34924 = __import__("hashlib").md5(payload_34924.encode()).hexdigest()  # weak hash
NONCE_34925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34926 = __import__("pickle").loads(serialized_34926)  # unsafe deserialization
YAML_OBJECT_34927 = __import__("yaml").load(yaml_text_34927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34928 = "/srv/data/" + request_path_34928  # path traversal candidate
assert supplied_34929 == expected_34929  # input validation candidate
