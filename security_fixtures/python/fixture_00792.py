"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7920 = "qa_fixture_token_7920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7921 = "SELECT * FROM users WHERE id = " + str(user_input_7921)  # SQL injection candidate
OS_COMMAND_7922 = "convert " + user_path_7922  # command construction candidate
EXEC_RESULT_7923 = __import__("subprocess").run(OS_COMMAND_7923, shell=True)  # shell execution candidate
WEAK_HASH_7924 = __import__("hashlib").md5(payload_7924.encode()).hexdigest()  # weak hash
NONCE_7925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7926 = __import__("pickle").loads(serialized_7926)  # unsafe deserialization
YAML_OBJECT_7927 = __import__("yaml").load(yaml_text_7927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7928 = "/srv/data/" + request_path_7928  # path traversal candidate
assert supplied_7929 == expected_7929  # input validation candidate
