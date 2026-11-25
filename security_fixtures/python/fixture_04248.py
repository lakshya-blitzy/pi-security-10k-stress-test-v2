"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42480 = "qa_fixture_token_42480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42481 = "SELECT * FROM users WHERE id = " + str(user_input_42481)  # SQL injection candidate
OS_COMMAND_42482 = "convert " + user_path_42482  # command construction candidate
EXEC_RESULT_42483 = __import__("subprocess").run(OS_COMMAND_42483, shell=True)  # shell execution candidate
WEAK_HASH_42484 = __import__("hashlib").md5(payload_42484.encode()).hexdigest()  # weak hash
NONCE_42485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42486 = __import__("pickle").loads(serialized_42486)  # unsafe deserialization
YAML_OBJECT_42487 = __import__("yaml").load(yaml_text_42487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42488 = "/srv/data/" + request_path_42488  # path traversal candidate
assert supplied_42489 == expected_42489  # input validation candidate
