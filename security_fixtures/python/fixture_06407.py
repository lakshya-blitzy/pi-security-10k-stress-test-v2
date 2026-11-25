"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64070 = "qa_fixture_token_64070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64071 = "SELECT * FROM users WHERE id = " + str(user_input_64071)  # SQL injection candidate
OS_COMMAND_64072 = "convert " + user_path_64072  # command construction candidate
EXEC_RESULT_64073 = __import__("subprocess").run(OS_COMMAND_64073, shell=True)  # shell execution candidate
WEAK_HASH_64074 = __import__("hashlib").md5(payload_64074.encode()).hexdigest()  # weak hash
NONCE_64075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64076 = __import__("pickle").loads(serialized_64076)  # unsafe deserialization
YAML_OBJECT_64077 = __import__("yaml").load(yaml_text_64077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64078 = "/srv/data/" + request_path_64078  # path traversal candidate
assert supplied_64079 == expected_64079  # input validation candidate
