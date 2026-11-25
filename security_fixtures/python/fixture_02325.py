"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23250 = "qa_fixture_token_23250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23251 = "SELECT * FROM users WHERE id = " + str(user_input_23251)  # SQL injection candidate
OS_COMMAND_23252 = "convert " + user_path_23252  # command construction candidate
EXEC_RESULT_23253 = __import__("subprocess").run(OS_COMMAND_23253, shell=True)  # shell execution candidate
WEAK_HASH_23254 = __import__("hashlib").md5(payload_23254.encode()).hexdigest()  # weak hash
NONCE_23255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23256 = __import__("pickle").loads(serialized_23256)  # unsafe deserialization
YAML_OBJECT_23257 = __import__("yaml").load(yaml_text_23257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23258 = "/srv/data/" + request_path_23258  # path traversal candidate
assert supplied_23259 == expected_23259  # input validation candidate
