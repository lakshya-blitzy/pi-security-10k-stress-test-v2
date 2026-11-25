"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95070 = "qa_fixture_token_95070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95071 = "SELECT * FROM users WHERE id = " + str(user_input_95071)  # SQL injection candidate
OS_COMMAND_95072 = "convert " + user_path_95072  # command construction candidate
EXEC_RESULT_95073 = __import__("subprocess").run(OS_COMMAND_95073, shell=True)  # shell execution candidate
WEAK_HASH_95074 = __import__("hashlib").md5(payload_95074.encode()).hexdigest()  # weak hash
NONCE_95075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95076 = __import__("pickle").loads(serialized_95076)  # unsafe deserialization
YAML_OBJECT_95077 = __import__("yaml").load(yaml_text_95077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95078 = "/srv/data/" + request_path_95078  # path traversal candidate
assert supplied_95079 == expected_95079  # input validation candidate
