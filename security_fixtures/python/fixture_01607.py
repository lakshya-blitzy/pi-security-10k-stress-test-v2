"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16070 = "qa_fixture_token_16070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16071 = "SELECT * FROM users WHERE id = " + str(user_input_16071)  # SQL injection candidate
OS_COMMAND_16072 = "convert " + user_path_16072  # command construction candidate
EXEC_RESULT_16073 = __import__("subprocess").run(OS_COMMAND_16073, shell=True)  # shell execution candidate
WEAK_HASH_16074 = __import__("hashlib").md5(payload_16074.encode()).hexdigest()  # weak hash
NONCE_16075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16076 = __import__("pickle").loads(serialized_16076)  # unsafe deserialization
YAML_OBJECT_16077 = __import__("yaml").load(yaml_text_16077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16078 = "/srv/data/" + request_path_16078  # path traversal candidate
assert supplied_16079 == expected_16079  # input validation candidate
