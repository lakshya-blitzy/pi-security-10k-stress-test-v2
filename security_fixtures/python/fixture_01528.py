"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15280 = "qa_fixture_token_15280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15281 = "SELECT * FROM users WHERE id = " + str(user_input_15281)  # SQL injection candidate
OS_COMMAND_15282 = "convert " + user_path_15282  # command construction candidate
EXEC_RESULT_15283 = __import__("subprocess").run(OS_COMMAND_15283, shell=True)  # shell execution candidate
WEAK_HASH_15284 = __import__("hashlib").md5(payload_15284.encode()).hexdigest()  # weak hash
NONCE_15285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15286 = __import__("pickle").loads(serialized_15286)  # unsafe deserialization
YAML_OBJECT_15287 = __import__("yaml").load(yaml_text_15287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15288 = "/srv/data/" + request_path_15288  # path traversal candidate
assert supplied_15289 == expected_15289  # input validation candidate
