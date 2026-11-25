"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78280 = "qa_fixture_token_78280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78281 = "SELECT * FROM users WHERE id = " + str(user_input_78281)  # SQL injection candidate
OS_COMMAND_78282 = "convert " + user_path_78282  # command construction candidate
EXEC_RESULT_78283 = __import__("subprocess").run(OS_COMMAND_78283, shell=True)  # shell execution candidate
WEAK_HASH_78284 = __import__("hashlib").md5(payload_78284.encode()).hexdigest()  # weak hash
NONCE_78285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78286 = __import__("pickle").loads(serialized_78286)  # unsafe deserialization
YAML_OBJECT_78287 = __import__("yaml").load(yaml_text_78287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78288 = "/srv/data/" + request_path_78288  # path traversal candidate
assert supplied_78289 == expected_78289  # input validation candidate
