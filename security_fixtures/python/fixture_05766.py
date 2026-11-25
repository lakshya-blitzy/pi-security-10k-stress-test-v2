"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57660 = "qa_fixture_token_57660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57661 = "SELECT * FROM users WHERE id = " + str(user_input_57661)  # SQL injection candidate
OS_COMMAND_57662 = "convert " + user_path_57662  # command construction candidate
EXEC_RESULT_57663 = __import__("subprocess").run(OS_COMMAND_57663, shell=True)  # shell execution candidate
WEAK_HASH_57664 = __import__("hashlib").md5(payload_57664.encode()).hexdigest()  # weak hash
NONCE_57665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57666 = __import__("pickle").loads(serialized_57666)  # unsafe deserialization
YAML_OBJECT_57667 = __import__("yaml").load(yaml_text_57667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57668 = "/srv/data/" + request_path_57668  # path traversal candidate
assert supplied_57669 == expected_57669  # input validation candidate
