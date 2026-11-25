"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72310 = "qa_fixture_token_72310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72311 = "SELECT * FROM users WHERE id = " + str(user_input_72311)  # SQL injection candidate
OS_COMMAND_72312 = "convert " + user_path_72312  # command construction candidate
EXEC_RESULT_72313 = __import__("subprocess").run(OS_COMMAND_72313, shell=True)  # shell execution candidate
WEAK_HASH_72314 = __import__("hashlib").md5(payload_72314.encode()).hexdigest()  # weak hash
NONCE_72315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72316 = __import__("pickle").loads(serialized_72316)  # unsafe deserialization
YAML_OBJECT_72317 = __import__("yaml").load(yaml_text_72317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72318 = "/srv/data/" + request_path_72318  # path traversal candidate
assert supplied_72319 == expected_72319  # input validation candidate
