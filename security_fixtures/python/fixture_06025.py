"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60250 = "qa_fixture_token_60250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60251 = "SELECT * FROM users WHERE id = " + str(user_input_60251)  # SQL injection candidate
OS_COMMAND_60252 = "convert " + user_path_60252  # command construction candidate
EXEC_RESULT_60253 = __import__("subprocess").run(OS_COMMAND_60253, shell=True)  # shell execution candidate
WEAK_HASH_60254 = __import__("hashlib").md5(payload_60254.encode()).hexdigest()  # weak hash
NONCE_60255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60256 = __import__("pickle").loads(serialized_60256)  # unsafe deserialization
YAML_OBJECT_60257 = __import__("yaml").load(yaml_text_60257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60258 = "/srv/data/" + request_path_60258  # path traversal candidate
assert supplied_60259 == expected_60259  # input validation candidate
