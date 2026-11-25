"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58480 = "qa_fixture_token_58480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58481 = "SELECT * FROM users WHERE id = " + str(user_input_58481)  # SQL injection candidate
OS_COMMAND_58482 = "convert " + user_path_58482  # command construction candidate
EXEC_RESULT_58483 = __import__("subprocess").run(OS_COMMAND_58483, shell=True)  # shell execution candidate
WEAK_HASH_58484 = __import__("hashlib").md5(payload_58484.encode()).hexdigest()  # weak hash
NONCE_58485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58486 = __import__("pickle").loads(serialized_58486)  # unsafe deserialization
YAML_OBJECT_58487 = __import__("yaml").load(yaml_text_58487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58488 = "/srv/data/" + request_path_58488  # path traversal candidate
assert supplied_58489 == expected_58489  # input validation candidate
