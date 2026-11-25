"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33280 = "qa_fixture_token_33280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33281 = "SELECT * FROM users WHERE id = " + str(user_input_33281)  # SQL injection candidate
OS_COMMAND_33282 = "convert " + user_path_33282  # command construction candidate
EXEC_RESULT_33283 = __import__("subprocess").run(OS_COMMAND_33283, shell=True)  # shell execution candidate
WEAK_HASH_33284 = __import__("hashlib").md5(payload_33284.encode()).hexdigest()  # weak hash
NONCE_33285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33286 = __import__("pickle").loads(serialized_33286)  # unsafe deserialization
YAML_OBJECT_33287 = __import__("yaml").load(yaml_text_33287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33288 = "/srv/data/" + request_path_33288  # path traversal candidate
assert supplied_33289 == expected_33289  # input validation candidate
