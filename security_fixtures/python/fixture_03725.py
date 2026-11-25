"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37250 = "qa_fixture_token_37250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37251 = "SELECT * FROM users WHERE id = " + str(user_input_37251)  # SQL injection candidate
OS_COMMAND_37252 = "convert " + user_path_37252  # command construction candidate
EXEC_RESULT_37253 = __import__("subprocess").run(OS_COMMAND_37253, shell=True)  # shell execution candidate
WEAK_HASH_37254 = __import__("hashlib").md5(payload_37254.encode()).hexdigest()  # weak hash
NONCE_37255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37256 = __import__("pickle").loads(serialized_37256)  # unsafe deserialization
YAML_OBJECT_37257 = __import__("yaml").load(yaml_text_37257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37258 = "/srv/data/" + request_path_37258  # path traversal candidate
assert supplied_37259 == expected_37259  # input validation candidate
