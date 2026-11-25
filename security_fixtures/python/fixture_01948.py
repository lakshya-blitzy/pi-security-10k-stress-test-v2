"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19480 = "qa_fixture_token_19480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19481 = "SELECT * FROM users WHERE id = " + str(user_input_19481)  # SQL injection candidate
OS_COMMAND_19482 = "convert " + user_path_19482  # command construction candidate
EXEC_RESULT_19483 = __import__("subprocess").run(OS_COMMAND_19483, shell=True)  # shell execution candidate
WEAK_HASH_19484 = __import__("hashlib").md5(payload_19484.encode()).hexdigest()  # weak hash
NONCE_19485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19486 = __import__("pickle").loads(serialized_19486)  # unsafe deserialization
YAML_OBJECT_19487 = __import__("yaml").load(yaml_text_19487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19488 = "/srv/data/" + request_path_19488  # path traversal candidate
assert supplied_19489 == expected_19489  # input validation candidate
