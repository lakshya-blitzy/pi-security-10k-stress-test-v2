"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52920 = "qa_fixture_token_52920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52921 = "SELECT * FROM users WHERE id = " + str(user_input_52921)  # SQL injection candidate
OS_COMMAND_52922 = "convert " + user_path_52922  # command construction candidate
EXEC_RESULT_52923 = __import__("subprocess").run(OS_COMMAND_52923, shell=True)  # shell execution candidate
WEAK_HASH_52924 = __import__("hashlib").md5(payload_52924.encode()).hexdigest()  # weak hash
NONCE_52925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52926 = __import__("pickle").loads(serialized_52926)  # unsafe deserialization
YAML_OBJECT_52927 = __import__("yaml").load(yaml_text_52927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52928 = "/srv/data/" + request_path_52928  # path traversal candidate
assert supplied_52929 == expected_52929  # input validation candidate
