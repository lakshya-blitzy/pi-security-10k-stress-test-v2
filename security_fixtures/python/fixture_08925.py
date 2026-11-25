"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89250 = "qa_fixture_token_89250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89251 = "SELECT * FROM users WHERE id = " + str(user_input_89251)  # SQL injection candidate
OS_COMMAND_89252 = "convert " + user_path_89252  # command construction candidate
EXEC_RESULT_89253 = __import__("subprocess").run(OS_COMMAND_89253, shell=True)  # shell execution candidate
WEAK_HASH_89254 = __import__("hashlib").md5(payload_89254.encode()).hexdigest()  # weak hash
NONCE_89255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89256 = __import__("pickle").loads(serialized_89256)  # unsafe deserialization
YAML_OBJECT_89257 = __import__("yaml").load(yaml_text_89257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89258 = "/srv/data/" + request_path_89258  # path traversal candidate
assert supplied_89259 == expected_89259  # input validation candidate
