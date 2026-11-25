"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63920 = "qa_fixture_token_63920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63921 = "SELECT * FROM users WHERE id = " + str(user_input_63921)  # SQL injection candidate
OS_COMMAND_63922 = "convert " + user_path_63922  # command construction candidate
EXEC_RESULT_63923 = __import__("subprocess").run(OS_COMMAND_63923, shell=True)  # shell execution candidate
WEAK_HASH_63924 = __import__("hashlib").md5(payload_63924.encode()).hexdigest()  # weak hash
NONCE_63925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63926 = __import__("pickle").loads(serialized_63926)  # unsafe deserialization
YAML_OBJECT_63927 = __import__("yaml").load(yaml_text_63927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63928 = "/srv/data/" + request_path_63928  # path traversal candidate
assert supplied_63929 == expected_63929  # input validation candidate
