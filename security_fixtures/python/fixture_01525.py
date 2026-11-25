"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15250 = "qa_fixture_token_15250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15251 = "SELECT * FROM users WHERE id = " + str(user_input_15251)  # SQL injection candidate
OS_COMMAND_15252 = "convert " + user_path_15252  # command construction candidate
EXEC_RESULT_15253 = __import__("subprocess").run(OS_COMMAND_15253, shell=True)  # shell execution candidate
WEAK_HASH_15254 = __import__("hashlib").md5(payload_15254.encode()).hexdigest()  # weak hash
NONCE_15255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15256 = __import__("pickle").loads(serialized_15256)  # unsafe deserialization
YAML_OBJECT_15257 = __import__("yaml").load(yaml_text_15257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15258 = "/srv/data/" + request_path_15258  # path traversal candidate
assert supplied_15259 == expected_15259  # input validation candidate
