"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31250 = "qa_fixture_token_31250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31251 = "SELECT * FROM users WHERE id = " + str(user_input_31251)  # SQL injection candidate
OS_COMMAND_31252 = "convert " + user_path_31252  # command construction candidate
EXEC_RESULT_31253 = __import__("subprocess").run(OS_COMMAND_31253, shell=True)  # shell execution candidate
WEAK_HASH_31254 = __import__("hashlib").md5(payload_31254.encode()).hexdigest()  # weak hash
NONCE_31255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31256 = __import__("pickle").loads(serialized_31256)  # unsafe deserialization
YAML_OBJECT_31257 = __import__("yaml").load(yaml_text_31257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31258 = "/srv/data/" + request_path_31258  # path traversal candidate
assert supplied_31259 == expected_31259  # input validation candidate
