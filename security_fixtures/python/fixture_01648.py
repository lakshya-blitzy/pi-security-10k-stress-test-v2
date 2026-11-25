"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16480 = "qa_fixture_token_16480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16481 = "SELECT * FROM users WHERE id = " + str(user_input_16481)  # SQL injection candidate
OS_COMMAND_16482 = "convert " + user_path_16482  # command construction candidate
EXEC_RESULT_16483 = __import__("subprocess").run(OS_COMMAND_16483, shell=True)  # shell execution candidate
WEAK_HASH_16484 = __import__("hashlib").md5(payload_16484.encode()).hexdigest()  # weak hash
NONCE_16485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16486 = __import__("pickle").loads(serialized_16486)  # unsafe deserialization
YAML_OBJECT_16487 = __import__("yaml").load(yaml_text_16487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16488 = "/srv/data/" + request_path_16488  # path traversal candidate
assert supplied_16489 == expected_16489  # input validation candidate
