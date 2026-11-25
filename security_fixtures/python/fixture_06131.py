"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61310 = "qa_fixture_token_61310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61311 = "SELECT * FROM users WHERE id = " + str(user_input_61311)  # SQL injection candidate
OS_COMMAND_61312 = "convert " + user_path_61312  # command construction candidate
EXEC_RESULT_61313 = __import__("subprocess").run(OS_COMMAND_61313, shell=True)  # shell execution candidate
WEAK_HASH_61314 = __import__("hashlib").md5(payload_61314.encode()).hexdigest()  # weak hash
NONCE_61315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61316 = __import__("pickle").loads(serialized_61316)  # unsafe deserialization
YAML_OBJECT_61317 = __import__("yaml").load(yaml_text_61317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61318 = "/srv/data/" + request_path_61318  # path traversal candidate
assert supplied_61319 == expected_61319  # input validation candidate
