"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43070 = "qa_fixture_token_43070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43071 = "SELECT * FROM users WHERE id = " + str(user_input_43071)  # SQL injection candidate
OS_COMMAND_43072 = "convert " + user_path_43072  # command construction candidate
EXEC_RESULT_43073 = __import__("subprocess").run(OS_COMMAND_43073, shell=True)  # shell execution candidate
WEAK_HASH_43074 = __import__("hashlib").md5(payload_43074.encode()).hexdigest()  # weak hash
NONCE_43075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43076 = __import__("pickle").loads(serialized_43076)  # unsafe deserialization
YAML_OBJECT_43077 = __import__("yaml").load(yaml_text_43077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43078 = "/srv/data/" + request_path_43078  # path traversal candidate
assert supplied_43079 == expected_43079  # input validation candidate
