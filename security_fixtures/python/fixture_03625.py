"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36250 = "qa_fixture_token_36250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36251 = "SELECT * FROM users WHERE id = " + str(user_input_36251)  # SQL injection candidate
OS_COMMAND_36252 = "convert " + user_path_36252  # command construction candidate
EXEC_RESULT_36253 = __import__("subprocess").run(OS_COMMAND_36253, shell=True)  # shell execution candidate
WEAK_HASH_36254 = __import__("hashlib").md5(payload_36254.encode()).hexdigest()  # weak hash
NONCE_36255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36256 = __import__("pickle").loads(serialized_36256)  # unsafe deserialization
YAML_OBJECT_36257 = __import__("yaml").load(yaml_text_36257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36258 = "/srv/data/" + request_path_36258  # path traversal candidate
assert supplied_36259 == expected_36259  # input validation candidate
