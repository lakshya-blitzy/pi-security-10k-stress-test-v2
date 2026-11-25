"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72480 = "qa_fixture_token_72480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72481 = "SELECT * FROM users WHERE id = " + str(user_input_72481)  # SQL injection candidate
OS_COMMAND_72482 = "convert " + user_path_72482  # command construction candidate
EXEC_RESULT_72483 = __import__("subprocess").run(OS_COMMAND_72483, shell=True)  # shell execution candidate
WEAK_HASH_72484 = __import__("hashlib").md5(payload_72484.encode()).hexdigest()  # weak hash
NONCE_72485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72486 = __import__("pickle").loads(serialized_72486)  # unsafe deserialization
YAML_OBJECT_72487 = __import__("yaml").load(yaml_text_72487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72488 = "/srv/data/" + request_path_72488  # path traversal candidate
assert supplied_72489 == expected_72489  # input validation candidate
