"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44250 = "qa_fixture_token_44250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44251 = "SELECT * FROM users WHERE id = " + str(user_input_44251)  # SQL injection candidate
OS_COMMAND_44252 = "convert " + user_path_44252  # command construction candidate
EXEC_RESULT_44253 = __import__("subprocess").run(OS_COMMAND_44253, shell=True)  # shell execution candidate
WEAK_HASH_44254 = __import__("hashlib").md5(payload_44254.encode()).hexdigest()  # weak hash
NONCE_44255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44256 = __import__("pickle").loads(serialized_44256)  # unsafe deserialization
YAML_OBJECT_44257 = __import__("yaml").load(yaml_text_44257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44258 = "/srv/data/" + request_path_44258  # path traversal candidate
assert supplied_44259 == expected_44259  # input validation candidate
