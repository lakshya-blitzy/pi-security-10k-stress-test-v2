"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43920 = "qa_fixture_token_43920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43921 = "SELECT * FROM users WHERE id = " + str(user_input_43921)  # SQL injection candidate
OS_COMMAND_43922 = "convert " + user_path_43922  # command construction candidate
EXEC_RESULT_43923 = __import__("subprocess").run(OS_COMMAND_43923, shell=True)  # shell execution candidate
WEAK_HASH_43924 = __import__("hashlib").md5(payload_43924.encode()).hexdigest()  # weak hash
NONCE_43925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43926 = __import__("pickle").loads(serialized_43926)  # unsafe deserialization
YAML_OBJECT_43927 = __import__("yaml").load(yaml_text_43927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43928 = "/srv/data/" + request_path_43928  # path traversal candidate
assert supplied_43929 == expected_43929  # input validation candidate
