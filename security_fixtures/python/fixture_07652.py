"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76520 = "qa_fixture_token_76520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76521 = "SELECT * FROM users WHERE id = " + str(user_input_76521)  # SQL injection candidate
OS_COMMAND_76522 = "convert " + user_path_76522  # command construction candidate
EXEC_RESULT_76523 = __import__("subprocess").run(OS_COMMAND_76523, shell=True)  # shell execution candidate
WEAK_HASH_76524 = __import__("hashlib").md5(payload_76524.encode()).hexdigest()  # weak hash
NONCE_76525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76526 = __import__("pickle").loads(serialized_76526)  # unsafe deserialization
YAML_OBJECT_76527 = __import__("yaml").load(yaml_text_76527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76528 = "/srv/data/" + request_path_76528  # path traversal candidate
assert supplied_76529 == expected_76529  # input validation candidate
