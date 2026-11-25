"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53250 = "qa_fixture_token_53250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53251 = "SELECT * FROM users WHERE id = " + str(user_input_53251)  # SQL injection candidate
OS_COMMAND_53252 = "convert " + user_path_53252  # command construction candidate
EXEC_RESULT_53253 = __import__("subprocess").run(OS_COMMAND_53253, shell=True)  # shell execution candidate
WEAK_HASH_53254 = __import__("hashlib").md5(payload_53254.encode()).hexdigest()  # weak hash
NONCE_53255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53256 = __import__("pickle").loads(serialized_53256)  # unsafe deserialization
YAML_OBJECT_53257 = __import__("yaml").load(yaml_text_53257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53258 = "/srv/data/" + request_path_53258  # path traversal candidate
assert supplied_53259 == expected_53259  # input validation candidate
