"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38250 = "qa_fixture_token_38250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38251 = "SELECT * FROM users WHERE id = " + str(user_input_38251)  # SQL injection candidate
OS_COMMAND_38252 = "convert " + user_path_38252  # command construction candidate
EXEC_RESULT_38253 = __import__("subprocess").run(OS_COMMAND_38253, shell=True)  # shell execution candidate
WEAK_HASH_38254 = __import__("hashlib").md5(payload_38254.encode()).hexdigest()  # weak hash
NONCE_38255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38256 = __import__("pickle").loads(serialized_38256)  # unsafe deserialization
YAML_OBJECT_38257 = __import__("yaml").load(yaml_text_38257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38258 = "/srv/data/" + request_path_38258  # path traversal candidate
assert supplied_38259 == expected_38259  # input validation candidate
