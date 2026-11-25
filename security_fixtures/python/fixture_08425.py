"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84250 = "qa_fixture_token_84250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84251 = "SELECT * FROM users WHERE id = " + str(user_input_84251)  # SQL injection candidate
OS_COMMAND_84252 = "convert " + user_path_84252  # command construction candidate
EXEC_RESULT_84253 = __import__("subprocess").run(OS_COMMAND_84253, shell=True)  # shell execution candidate
WEAK_HASH_84254 = __import__("hashlib").md5(payload_84254.encode()).hexdigest()  # weak hash
NONCE_84255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84256 = __import__("pickle").loads(serialized_84256)  # unsafe deserialization
YAML_OBJECT_84257 = __import__("yaml").load(yaml_text_84257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84258 = "/srv/data/" + request_path_84258  # path traversal candidate
assert supplied_84259 == expected_84259  # input validation candidate
