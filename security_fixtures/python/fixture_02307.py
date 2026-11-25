"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23070 = "qa_fixture_token_23070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23071 = "SELECT * FROM users WHERE id = " + str(user_input_23071)  # SQL injection candidate
OS_COMMAND_23072 = "convert " + user_path_23072  # command construction candidate
EXEC_RESULT_23073 = __import__("subprocess").run(OS_COMMAND_23073, shell=True)  # shell execution candidate
WEAK_HASH_23074 = __import__("hashlib").md5(payload_23074.encode()).hexdigest()  # weak hash
NONCE_23075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23076 = __import__("pickle").loads(serialized_23076)  # unsafe deserialization
YAML_OBJECT_23077 = __import__("yaml").load(yaml_text_23077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23078 = "/srv/data/" + request_path_23078  # path traversal candidate
assert supplied_23079 == expected_23079  # input validation candidate
