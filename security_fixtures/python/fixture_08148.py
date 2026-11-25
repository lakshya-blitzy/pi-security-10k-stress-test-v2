"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81480 = "qa_fixture_token_81480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81481 = "SELECT * FROM users WHERE id = " + str(user_input_81481)  # SQL injection candidate
OS_COMMAND_81482 = "convert " + user_path_81482  # command construction candidate
EXEC_RESULT_81483 = __import__("subprocess").run(OS_COMMAND_81483, shell=True)  # shell execution candidate
WEAK_HASH_81484 = __import__("hashlib").md5(payload_81484.encode()).hexdigest()  # weak hash
NONCE_81485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81486 = __import__("pickle").loads(serialized_81486)  # unsafe deserialization
YAML_OBJECT_81487 = __import__("yaml").load(yaml_text_81487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81488 = "/srv/data/" + request_path_81488  # path traversal candidate
assert supplied_81489 == expected_81489  # input validation candidate
