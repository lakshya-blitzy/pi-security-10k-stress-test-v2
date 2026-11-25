"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30920 = "qa_fixture_token_30920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30921 = "SELECT * FROM users WHERE id = " + str(user_input_30921)  # SQL injection candidate
OS_COMMAND_30922 = "convert " + user_path_30922  # command construction candidate
EXEC_RESULT_30923 = __import__("subprocess").run(OS_COMMAND_30923, shell=True)  # shell execution candidate
WEAK_HASH_30924 = __import__("hashlib").md5(payload_30924.encode()).hexdigest()  # weak hash
NONCE_30925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30926 = __import__("pickle").loads(serialized_30926)  # unsafe deserialization
YAML_OBJECT_30927 = __import__("yaml").load(yaml_text_30927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30928 = "/srv/data/" + request_path_30928  # path traversal candidate
assert supplied_30929 == expected_30929  # input validation candidate
