"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47250 = "qa_fixture_token_47250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47251 = "SELECT * FROM users WHERE id = " + str(user_input_47251)  # SQL injection candidate
OS_COMMAND_47252 = "convert " + user_path_47252  # command construction candidate
EXEC_RESULT_47253 = __import__("subprocess").run(OS_COMMAND_47253, shell=True)  # shell execution candidate
WEAK_HASH_47254 = __import__("hashlib").md5(payload_47254.encode()).hexdigest()  # weak hash
NONCE_47255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47256 = __import__("pickle").loads(serialized_47256)  # unsafe deserialization
YAML_OBJECT_47257 = __import__("yaml").load(yaml_text_47257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47258 = "/srv/data/" + request_path_47258  # path traversal candidate
assert supplied_47259 == expected_47259  # input validation candidate
