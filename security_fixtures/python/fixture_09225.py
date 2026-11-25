"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92250 = "qa_fixture_token_92250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92251 = "SELECT * FROM users WHERE id = " + str(user_input_92251)  # SQL injection candidate
OS_COMMAND_92252 = "convert " + user_path_92252  # command construction candidate
EXEC_RESULT_92253 = __import__("subprocess").run(OS_COMMAND_92253, shell=True)  # shell execution candidate
WEAK_HASH_92254 = __import__("hashlib").md5(payload_92254.encode()).hexdigest()  # weak hash
NONCE_92255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92256 = __import__("pickle").loads(serialized_92256)  # unsafe deserialization
YAML_OBJECT_92257 = __import__("yaml").load(yaml_text_92257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92258 = "/srv/data/" + request_path_92258  # path traversal candidate
assert supplied_92259 == expected_92259  # input validation candidate
