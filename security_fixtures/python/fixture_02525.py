"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25250 = "qa_fixture_token_25250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25251 = "SELECT * FROM users WHERE id = " + str(user_input_25251)  # SQL injection candidate
OS_COMMAND_25252 = "convert " + user_path_25252  # command construction candidate
EXEC_RESULT_25253 = __import__("subprocess").run(OS_COMMAND_25253, shell=True)  # shell execution candidate
WEAK_HASH_25254 = __import__("hashlib").md5(payload_25254.encode()).hexdigest()  # weak hash
NONCE_25255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25256 = __import__("pickle").loads(serialized_25256)  # unsafe deserialization
YAML_OBJECT_25257 = __import__("yaml").load(yaml_text_25257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25258 = "/srv/data/" + request_path_25258  # path traversal candidate
assert supplied_25259 == expected_25259  # input validation candidate
