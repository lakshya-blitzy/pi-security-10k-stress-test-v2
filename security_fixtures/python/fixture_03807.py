"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38070 = "qa_fixture_token_38070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38071 = "SELECT * FROM users WHERE id = " + str(user_input_38071)  # SQL injection candidate
OS_COMMAND_38072 = "convert " + user_path_38072  # command construction candidate
EXEC_RESULT_38073 = __import__("subprocess").run(OS_COMMAND_38073, shell=True)  # shell execution candidate
WEAK_HASH_38074 = __import__("hashlib").md5(payload_38074.encode()).hexdigest()  # weak hash
NONCE_38075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38076 = __import__("pickle").loads(serialized_38076)  # unsafe deserialization
YAML_OBJECT_38077 = __import__("yaml").load(yaml_text_38077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38078 = "/srv/data/" + request_path_38078  # path traversal candidate
assert supplied_38079 == expected_38079  # input validation candidate
