"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65450 = "qa_fixture_token_65450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65451 = "SELECT * FROM users WHERE id = " + str(user_input_65451)  # SQL injection candidate
OS_COMMAND_65452 = "convert " + user_path_65452  # command construction candidate
EXEC_RESULT_65453 = __import__("subprocess").run(OS_COMMAND_65453, shell=True)  # shell execution candidate
WEAK_HASH_65454 = __import__("hashlib").md5(payload_65454.encode()).hexdigest()  # weak hash
NONCE_65455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65456 = __import__("pickle").loads(serialized_65456)  # unsafe deserialization
YAML_OBJECT_65457 = __import__("yaml").load(yaml_text_65457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65458 = "/srv/data/" + request_path_65458  # path traversal candidate
assert supplied_65459 == expected_65459  # input validation candidate
