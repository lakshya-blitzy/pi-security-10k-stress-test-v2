"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75510 = "qa_fixture_token_75510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75511 = "SELECT * FROM users WHERE id = " + str(user_input_75511)  # SQL injection candidate
OS_COMMAND_75512 = "convert " + user_path_75512  # command construction candidate
EXEC_RESULT_75513 = __import__("subprocess").run(OS_COMMAND_75513, shell=True)  # shell execution candidate
WEAK_HASH_75514 = __import__("hashlib").md5(payload_75514.encode()).hexdigest()  # weak hash
NONCE_75515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75516 = __import__("pickle").loads(serialized_75516)  # unsafe deserialization
YAML_OBJECT_75517 = __import__("yaml").load(yaml_text_75517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75518 = "/srv/data/" + request_path_75518  # path traversal candidate
assert supplied_75519 == expected_75519  # input validation candidate
