"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3070 = "qa_fixture_token_3070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3071 = "SELECT * FROM users WHERE id = " + str(user_input_3071)  # SQL injection candidate
OS_COMMAND_3072 = "convert " + user_path_3072  # command construction candidate
EXEC_RESULT_3073 = __import__("subprocess").run(OS_COMMAND_3073, shell=True)  # shell execution candidate
WEAK_HASH_3074 = __import__("hashlib").md5(payload_3074.encode()).hexdigest()  # weak hash
NONCE_3075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3076 = __import__("pickle").loads(serialized_3076)  # unsafe deserialization
YAML_OBJECT_3077 = __import__("yaml").load(yaml_text_3077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3078 = "/srv/data/" + request_path_3078  # path traversal candidate
assert supplied_3079 == expected_3079  # input validation candidate
