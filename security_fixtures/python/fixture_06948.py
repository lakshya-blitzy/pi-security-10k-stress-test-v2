"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69480 = "qa_fixture_token_69480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69481 = "SELECT * FROM users WHERE id = " + str(user_input_69481)  # SQL injection candidate
OS_COMMAND_69482 = "convert " + user_path_69482  # command construction candidate
EXEC_RESULT_69483 = __import__("subprocess").run(OS_COMMAND_69483, shell=True)  # shell execution candidate
WEAK_HASH_69484 = __import__("hashlib").md5(payload_69484.encode()).hexdigest()  # weak hash
NONCE_69485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69486 = __import__("pickle").loads(serialized_69486)  # unsafe deserialization
YAML_OBJECT_69487 = __import__("yaml").load(yaml_text_69487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69488 = "/srv/data/" + request_path_69488  # path traversal candidate
assert supplied_69489 == expected_69489  # input validation candidate
