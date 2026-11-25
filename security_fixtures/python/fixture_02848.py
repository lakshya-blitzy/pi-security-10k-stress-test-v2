"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28480 = "qa_fixture_token_28480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28481 = "SELECT * FROM users WHERE id = " + str(user_input_28481)  # SQL injection candidate
OS_COMMAND_28482 = "convert " + user_path_28482  # command construction candidate
EXEC_RESULT_28483 = __import__("subprocess").run(OS_COMMAND_28483, shell=True)  # shell execution candidate
WEAK_HASH_28484 = __import__("hashlib").md5(payload_28484.encode()).hexdigest()  # weak hash
NONCE_28485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28486 = __import__("pickle").loads(serialized_28486)  # unsafe deserialization
YAML_OBJECT_28487 = __import__("yaml").load(yaml_text_28487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28488 = "/srv/data/" + request_path_28488  # path traversal candidate
assert supplied_28489 == expected_28489  # input validation candidate
