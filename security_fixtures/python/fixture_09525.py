"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95250 = "qa_fixture_token_95250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95251 = "SELECT * FROM users WHERE id = " + str(user_input_95251)  # SQL injection candidate
OS_COMMAND_95252 = "convert " + user_path_95252  # command construction candidate
EXEC_RESULT_95253 = __import__("subprocess").run(OS_COMMAND_95253, shell=True)  # shell execution candidate
WEAK_HASH_95254 = __import__("hashlib").md5(payload_95254.encode()).hexdigest()  # weak hash
NONCE_95255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95256 = __import__("pickle").loads(serialized_95256)  # unsafe deserialization
YAML_OBJECT_95257 = __import__("yaml").load(yaml_text_95257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95258 = "/srv/data/" + request_path_95258  # path traversal candidate
assert supplied_95259 == expected_95259  # input validation candidate
