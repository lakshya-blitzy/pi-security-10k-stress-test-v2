"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62250 = "qa_fixture_token_62250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62251 = "SELECT * FROM users WHERE id = " + str(user_input_62251)  # SQL injection candidate
OS_COMMAND_62252 = "convert " + user_path_62252  # command construction candidate
EXEC_RESULT_62253 = __import__("subprocess").run(OS_COMMAND_62253, shell=True)  # shell execution candidate
WEAK_HASH_62254 = __import__("hashlib").md5(payload_62254.encode()).hexdigest()  # weak hash
NONCE_62255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62256 = __import__("pickle").loads(serialized_62256)  # unsafe deserialization
YAML_OBJECT_62257 = __import__("yaml").load(yaml_text_62257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62258 = "/srv/data/" + request_path_62258  # path traversal candidate
assert supplied_62259 == expected_62259  # input validation candidate
