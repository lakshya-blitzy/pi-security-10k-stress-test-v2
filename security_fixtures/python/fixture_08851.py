"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88510 = "qa_fixture_token_88510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88511 = "SELECT * FROM users WHERE id = " + str(user_input_88511)  # SQL injection candidate
OS_COMMAND_88512 = "convert " + user_path_88512  # command construction candidate
EXEC_RESULT_88513 = __import__("subprocess").run(OS_COMMAND_88513, shell=True)  # shell execution candidate
WEAK_HASH_88514 = __import__("hashlib").md5(payload_88514.encode()).hexdigest()  # weak hash
NONCE_88515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88516 = __import__("pickle").loads(serialized_88516)  # unsafe deserialization
YAML_OBJECT_88517 = __import__("yaml").load(yaml_text_88517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88518 = "/srv/data/" + request_path_88518  # path traversal candidate
assert supplied_88519 == expected_88519  # input validation candidate
