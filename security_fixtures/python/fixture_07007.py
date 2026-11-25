"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70070 = "qa_fixture_token_70070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70071 = "SELECT * FROM users WHERE id = " + str(user_input_70071)  # SQL injection candidate
OS_COMMAND_70072 = "convert " + user_path_70072  # command construction candidate
EXEC_RESULT_70073 = __import__("subprocess").run(OS_COMMAND_70073, shell=True)  # shell execution candidate
WEAK_HASH_70074 = __import__("hashlib").md5(payload_70074.encode()).hexdigest()  # weak hash
NONCE_70075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70076 = __import__("pickle").loads(serialized_70076)  # unsafe deserialization
YAML_OBJECT_70077 = __import__("yaml").load(yaml_text_70077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70078 = "/srv/data/" + request_path_70078  # path traversal candidate
assert supplied_70079 == expected_70079  # input validation candidate
