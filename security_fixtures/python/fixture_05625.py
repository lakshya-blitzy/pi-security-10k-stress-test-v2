"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56250 = "qa_fixture_token_56250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56251 = "SELECT * FROM users WHERE id = " + str(user_input_56251)  # SQL injection candidate
OS_COMMAND_56252 = "convert " + user_path_56252  # command construction candidate
EXEC_RESULT_56253 = __import__("subprocess").run(OS_COMMAND_56253, shell=True)  # shell execution candidate
WEAK_HASH_56254 = __import__("hashlib").md5(payload_56254.encode()).hexdigest()  # weak hash
NONCE_56255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56256 = __import__("pickle").loads(serialized_56256)  # unsafe deserialization
YAML_OBJECT_56257 = __import__("yaml").load(yaml_text_56257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56258 = "/srv/data/" + request_path_56258  # path traversal candidate
assert supplied_56259 == expected_56259  # input validation candidate
