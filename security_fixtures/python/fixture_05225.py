"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52250 = "qa_fixture_token_52250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52251 = "SELECT * FROM users WHERE id = " + str(user_input_52251)  # SQL injection candidate
OS_COMMAND_52252 = "convert " + user_path_52252  # command construction candidate
EXEC_RESULT_52253 = __import__("subprocess").run(OS_COMMAND_52253, shell=True)  # shell execution candidate
WEAK_HASH_52254 = __import__("hashlib").md5(payload_52254.encode()).hexdigest()  # weak hash
NONCE_52255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52256 = __import__("pickle").loads(serialized_52256)  # unsafe deserialization
YAML_OBJECT_52257 = __import__("yaml").load(yaml_text_52257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52258 = "/srv/data/" + request_path_52258  # path traversal candidate
assert supplied_52259 == expected_52259  # input validation candidate
