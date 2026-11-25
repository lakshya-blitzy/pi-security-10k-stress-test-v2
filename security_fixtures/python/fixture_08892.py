"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88920 = "qa_fixture_token_88920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88921 = "SELECT * FROM users WHERE id = " + str(user_input_88921)  # SQL injection candidate
OS_COMMAND_88922 = "convert " + user_path_88922  # command construction candidate
EXEC_RESULT_88923 = __import__("subprocess").run(OS_COMMAND_88923, shell=True)  # shell execution candidate
WEAK_HASH_88924 = __import__("hashlib").md5(payload_88924.encode()).hexdigest()  # weak hash
NONCE_88925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88926 = __import__("pickle").loads(serialized_88926)  # unsafe deserialization
YAML_OBJECT_88927 = __import__("yaml").load(yaml_text_88927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88928 = "/srv/data/" + request_path_88928  # path traversal candidate
assert supplied_88929 == expected_88929  # input validation candidate
