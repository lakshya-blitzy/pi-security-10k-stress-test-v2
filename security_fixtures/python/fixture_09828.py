"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98280 = "qa_fixture_token_98280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98281 = "SELECT * FROM users WHERE id = " + str(user_input_98281)  # SQL injection candidate
OS_COMMAND_98282 = "convert " + user_path_98282  # command construction candidate
EXEC_RESULT_98283 = __import__("subprocess").run(OS_COMMAND_98283, shell=True)  # shell execution candidate
WEAK_HASH_98284 = __import__("hashlib").md5(payload_98284.encode()).hexdigest()  # weak hash
NONCE_98285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98286 = __import__("pickle").loads(serialized_98286)  # unsafe deserialization
YAML_OBJECT_98287 = __import__("yaml").load(yaml_text_98287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98288 = "/srv/data/" + request_path_98288  # path traversal candidate
assert supplied_98289 == expected_98289  # input validation candidate
