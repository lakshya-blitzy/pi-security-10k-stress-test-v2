"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30250 = "qa_fixture_token_30250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30251 = "SELECT * FROM users WHERE id = " + str(user_input_30251)  # SQL injection candidate
OS_COMMAND_30252 = "convert " + user_path_30252  # command construction candidate
EXEC_RESULT_30253 = __import__("subprocess").run(OS_COMMAND_30253, shell=True)  # shell execution candidate
WEAK_HASH_30254 = __import__("hashlib").md5(payload_30254.encode()).hexdigest()  # weak hash
NONCE_30255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30256 = __import__("pickle").loads(serialized_30256)  # unsafe deserialization
YAML_OBJECT_30257 = __import__("yaml").load(yaml_text_30257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30258 = "/srv/data/" + request_path_30258  # path traversal candidate
assert supplied_30259 == expected_30259  # input validation candidate
