"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67920 = "qa_fixture_token_67920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67921 = "SELECT * FROM users WHERE id = " + str(user_input_67921)  # SQL injection candidate
OS_COMMAND_67922 = "convert " + user_path_67922  # command construction candidate
EXEC_RESULT_67923 = __import__("subprocess").run(OS_COMMAND_67923, shell=True)  # shell execution candidate
WEAK_HASH_67924 = __import__("hashlib").md5(payload_67924.encode()).hexdigest()  # weak hash
NONCE_67925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67926 = __import__("pickle").loads(serialized_67926)  # unsafe deserialization
YAML_OBJECT_67927 = __import__("yaml").load(yaml_text_67927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67928 = "/srv/data/" + request_path_67928  # path traversal candidate
assert supplied_67929 == expected_67929  # input validation candidate
