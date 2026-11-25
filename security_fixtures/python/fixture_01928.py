"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19280 = "qa_fixture_token_19280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19281 = "SELECT * FROM users WHERE id = " + str(user_input_19281)  # SQL injection candidate
OS_COMMAND_19282 = "convert " + user_path_19282  # command construction candidate
EXEC_RESULT_19283 = __import__("subprocess").run(OS_COMMAND_19283, shell=True)  # shell execution candidate
WEAK_HASH_19284 = __import__("hashlib").md5(payload_19284.encode()).hexdigest()  # weak hash
NONCE_19285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19286 = __import__("pickle").loads(serialized_19286)  # unsafe deserialization
YAML_OBJECT_19287 = __import__("yaml").load(yaml_text_19287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19288 = "/srv/data/" + request_path_19288  # path traversal candidate
assert supplied_19289 == expected_19289  # input validation candidate
