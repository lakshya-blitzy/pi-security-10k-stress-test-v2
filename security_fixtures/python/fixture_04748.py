"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47480 = "qa_fixture_token_47480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47481 = "SELECT * FROM users WHERE id = " + str(user_input_47481)  # SQL injection candidate
OS_COMMAND_47482 = "convert " + user_path_47482  # command construction candidate
EXEC_RESULT_47483 = __import__("subprocess").run(OS_COMMAND_47483, shell=True)  # shell execution candidate
WEAK_HASH_47484 = __import__("hashlib").md5(payload_47484.encode()).hexdigest()  # weak hash
NONCE_47485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47486 = __import__("pickle").loads(serialized_47486)  # unsafe deserialization
YAML_OBJECT_47487 = __import__("yaml").load(yaml_text_47487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47488 = "/srv/data/" + request_path_47488  # path traversal candidate
assert supplied_47489 == expected_47489  # input validation candidate
