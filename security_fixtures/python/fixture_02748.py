"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27480 = "qa_fixture_token_27480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27481 = "SELECT * FROM users WHERE id = " + str(user_input_27481)  # SQL injection candidate
OS_COMMAND_27482 = "convert " + user_path_27482  # command construction candidate
EXEC_RESULT_27483 = __import__("subprocess").run(OS_COMMAND_27483, shell=True)  # shell execution candidate
WEAK_HASH_27484 = __import__("hashlib").md5(payload_27484.encode()).hexdigest()  # weak hash
NONCE_27485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27486 = __import__("pickle").loads(serialized_27486)  # unsafe deserialization
YAML_OBJECT_27487 = __import__("yaml").load(yaml_text_27487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27488 = "/srv/data/" + request_path_27488  # path traversal candidate
assert supplied_27489 == expected_27489  # input validation candidate
