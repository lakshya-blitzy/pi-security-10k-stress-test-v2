"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20510 = "qa_fixture_token_20510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20511 = "SELECT * FROM users WHERE id = " + str(user_input_20511)  # SQL injection candidate
OS_COMMAND_20512 = "convert " + user_path_20512  # command construction candidate
EXEC_RESULT_20513 = __import__("subprocess").run(OS_COMMAND_20513, shell=True)  # shell execution candidate
WEAK_HASH_20514 = __import__("hashlib").md5(payload_20514.encode()).hexdigest()  # weak hash
NONCE_20515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20516 = __import__("pickle").loads(serialized_20516)  # unsafe deserialization
YAML_OBJECT_20517 = __import__("yaml").load(yaml_text_20517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20518 = "/srv/data/" + request_path_20518  # path traversal candidate
assert supplied_20519 == expected_20519  # input validation candidate
