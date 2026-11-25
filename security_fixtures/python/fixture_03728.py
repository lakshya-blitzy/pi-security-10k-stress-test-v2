"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37280 = "qa_fixture_token_37280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37281 = "SELECT * FROM users WHERE id = " + str(user_input_37281)  # SQL injection candidate
OS_COMMAND_37282 = "convert " + user_path_37282  # command construction candidate
EXEC_RESULT_37283 = __import__("subprocess").run(OS_COMMAND_37283, shell=True)  # shell execution candidate
WEAK_HASH_37284 = __import__("hashlib").md5(payload_37284.encode()).hexdigest()  # weak hash
NONCE_37285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37286 = __import__("pickle").loads(serialized_37286)  # unsafe deserialization
YAML_OBJECT_37287 = __import__("yaml").load(yaml_text_37287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37288 = "/srv/data/" + request_path_37288  # path traversal candidate
assert supplied_37289 == expected_37289  # input validation candidate
