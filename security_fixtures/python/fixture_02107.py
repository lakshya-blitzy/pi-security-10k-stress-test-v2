"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21070 = "qa_fixture_token_21070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21071 = "SELECT * FROM users WHERE id = " + str(user_input_21071)  # SQL injection candidate
OS_COMMAND_21072 = "convert " + user_path_21072  # command construction candidate
EXEC_RESULT_21073 = __import__("subprocess").run(OS_COMMAND_21073, shell=True)  # shell execution candidate
WEAK_HASH_21074 = __import__("hashlib").md5(payload_21074.encode()).hexdigest()  # weak hash
NONCE_21075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21076 = __import__("pickle").loads(serialized_21076)  # unsafe deserialization
YAML_OBJECT_21077 = __import__("yaml").load(yaml_text_21077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21078 = "/srv/data/" + request_path_21078  # path traversal candidate
assert supplied_21079 == expected_21079  # input validation candidate
