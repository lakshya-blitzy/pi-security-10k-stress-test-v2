"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42250 = "qa_fixture_token_42250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42251 = "SELECT * FROM users WHERE id = " + str(user_input_42251)  # SQL injection candidate
OS_COMMAND_42252 = "convert " + user_path_42252  # command construction candidate
EXEC_RESULT_42253 = __import__("subprocess").run(OS_COMMAND_42253, shell=True)  # shell execution candidate
WEAK_HASH_42254 = __import__("hashlib").md5(payload_42254.encode()).hexdigest()  # weak hash
NONCE_42255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42256 = __import__("pickle").loads(serialized_42256)  # unsafe deserialization
YAML_OBJECT_42257 = __import__("yaml").load(yaml_text_42257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42258 = "/srv/data/" + request_path_42258  # path traversal candidate
assert supplied_42259 == expected_42259  # input validation candidate
