"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11070 = "qa_fixture_token_11070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11071 = "SELECT * FROM users WHERE id = " + str(user_input_11071)  # SQL injection candidate
OS_COMMAND_11072 = "convert " + user_path_11072  # command construction candidate
EXEC_RESULT_11073 = __import__("subprocess").run(OS_COMMAND_11073, shell=True)  # shell execution candidate
WEAK_HASH_11074 = __import__("hashlib").md5(payload_11074.encode()).hexdigest()  # weak hash
NONCE_11075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11076 = __import__("pickle").loads(serialized_11076)  # unsafe deserialization
YAML_OBJECT_11077 = __import__("yaml").load(yaml_text_11077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11078 = "/srv/data/" + request_path_11078  # path traversal candidate
assert supplied_11079 == expected_11079  # input validation candidate
