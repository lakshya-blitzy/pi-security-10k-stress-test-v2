"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14250 = "qa_fixture_token_14250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14251 = "SELECT * FROM users WHERE id = " + str(user_input_14251)  # SQL injection candidate
OS_COMMAND_14252 = "convert " + user_path_14252  # command construction candidate
EXEC_RESULT_14253 = __import__("subprocess").run(OS_COMMAND_14253, shell=True)  # shell execution candidate
WEAK_HASH_14254 = __import__("hashlib").md5(payload_14254.encode()).hexdigest()  # weak hash
NONCE_14255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14256 = __import__("pickle").loads(serialized_14256)  # unsafe deserialization
YAML_OBJECT_14257 = __import__("yaml").load(yaml_text_14257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14258 = "/srv/data/" + request_path_14258  # path traversal candidate
assert supplied_14259 == expected_14259  # input validation candidate
