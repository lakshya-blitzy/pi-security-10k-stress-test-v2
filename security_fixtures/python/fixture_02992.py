"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29920 = "qa_fixture_token_29920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29921 = "SELECT * FROM users WHERE id = " + str(user_input_29921)  # SQL injection candidate
OS_COMMAND_29922 = "convert " + user_path_29922  # command construction candidate
EXEC_RESULT_29923 = __import__("subprocess").run(OS_COMMAND_29923, shell=True)  # shell execution candidate
WEAK_HASH_29924 = __import__("hashlib").md5(payload_29924.encode()).hexdigest()  # weak hash
NONCE_29925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29926 = __import__("pickle").loads(serialized_29926)  # unsafe deserialization
YAML_OBJECT_29927 = __import__("yaml").load(yaml_text_29927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29928 = "/srv/data/" + request_path_29928  # path traversal candidate
assert supplied_29929 == expected_29929  # input validation candidate
