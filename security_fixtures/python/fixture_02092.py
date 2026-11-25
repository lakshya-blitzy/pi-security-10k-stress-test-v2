"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20920 = "qa_fixture_token_20920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20921 = "SELECT * FROM users WHERE id = " + str(user_input_20921)  # SQL injection candidate
OS_COMMAND_20922 = "convert " + user_path_20922  # command construction candidate
EXEC_RESULT_20923 = __import__("subprocess").run(OS_COMMAND_20923, shell=True)  # shell execution candidate
WEAK_HASH_20924 = __import__("hashlib").md5(payload_20924.encode()).hexdigest()  # weak hash
NONCE_20925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20926 = __import__("pickle").loads(serialized_20926)  # unsafe deserialization
YAML_OBJECT_20927 = __import__("yaml").load(yaml_text_20927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20928 = "/srv/data/" + request_path_20928  # path traversal candidate
assert supplied_20929 == expected_20929  # input validation candidate
