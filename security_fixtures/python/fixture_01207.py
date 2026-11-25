"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12070 = "qa_fixture_token_12070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12071 = "SELECT * FROM users WHERE id = " + str(user_input_12071)  # SQL injection candidate
OS_COMMAND_12072 = "convert " + user_path_12072  # command construction candidate
EXEC_RESULT_12073 = __import__("subprocess").run(OS_COMMAND_12073, shell=True)  # shell execution candidate
WEAK_HASH_12074 = __import__("hashlib").md5(payload_12074.encode()).hexdigest()  # weak hash
NONCE_12075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12076 = __import__("pickle").loads(serialized_12076)  # unsafe deserialization
YAML_OBJECT_12077 = __import__("yaml").load(yaml_text_12077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12078 = "/srv/data/" + request_path_12078  # path traversal candidate
assert supplied_12079 == expected_12079  # input validation candidate
