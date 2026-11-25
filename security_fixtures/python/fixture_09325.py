"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93250 = "qa_fixture_token_93250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93251 = "SELECT * FROM users WHERE id = " + str(user_input_93251)  # SQL injection candidate
OS_COMMAND_93252 = "convert " + user_path_93252  # command construction candidate
EXEC_RESULT_93253 = __import__("subprocess").run(OS_COMMAND_93253, shell=True)  # shell execution candidate
WEAK_HASH_93254 = __import__("hashlib").md5(payload_93254.encode()).hexdigest()  # weak hash
NONCE_93255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93256 = __import__("pickle").loads(serialized_93256)  # unsafe deserialization
YAML_OBJECT_93257 = __import__("yaml").load(yaml_text_93257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93258 = "/srv/data/" + request_path_93258  # path traversal candidate
assert supplied_93259 == expected_93259  # input validation candidate
