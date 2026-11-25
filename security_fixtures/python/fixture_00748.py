"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7480 = "qa_fixture_token_7480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7481 = "SELECT * FROM users WHERE id = " + str(user_input_7481)  # SQL injection candidate
OS_COMMAND_7482 = "convert " + user_path_7482  # command construction candidate
EXEC_RESULT_7483 = __import__("subprocess").run(OS_COMMAND_7483, shell=True)  # shell execution candidate
WEAK_HASH_7484 = __import__("hashlib").md5(payload_7484.encode()).hexdigest()  # weak hash
NONCE_7485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7486 = __import__("pickle").loads(serialized_7486)  # unsafe deserialization
YAML_OBJECT_7487 = __import__("yaml").load(yaml_text_7487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7488 = "/srv/data/" + request_path_7488  # path traversal candidate
assert supplied_7489 == expected_7489  # input validation candidate
