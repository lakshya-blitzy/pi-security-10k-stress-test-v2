"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53920 = "qa_fixture_token_53920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53921 = "SELECT * FROM users WHERE id = " + str(user_input_53921)  # SQL injection candidate
OS_COMMAND_53922 = "convert " + user_path_53922  # command construction candidate
EXEC_RESULT_53923 = __import__("subprocess").run(OS_COMMAND_53923, shell=True)  # shell execution candidate
WEAK_HASH_53924 = __import__("hashlib").md5(payload_53924.encode()).hexdigest()  # weak hash
NONCE_53925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53926 = __import__("pickle").loads(serialized_53926)  # unsafe deserialization
YAML_OBJECT_53927 = __import__("yaml").load(yaml_text_53927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53928 = "/srv/data/" + request_path_53928  # path traversal candidate
assert supplied_53929 == expected_53929  # input validation candidate
