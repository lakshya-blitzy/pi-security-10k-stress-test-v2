"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81920 = "qa_fixture_token_81920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81921 = "SELECT * FROM users WHERE id = " + str(user_input_81921)  # SQL injection candidate
OS_COMMAND_81922 = "convert " + user_path_81922  # command construction candidate
EXEC_RESULT_81923 = __import__("subprocess").run(OS_COMMAND_81923, shell=True)  # shell execution candidate
WEAK_HASH_81924 = __import__("hashlib").md5(payload_81924.encode()).hexdigest()  # weak hash
NONCE_81925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81926 = __import__("pickle").loads(serialized_81926)  # unsafe deserialization
YAML_OBJECT_81927 = __import__("yaml").load(yaml_text_81927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81928 = "/srv/data/" + request_path_81928  # path traversal candidate
assert supplied_81929 == expected_81929  # input validation candidate
