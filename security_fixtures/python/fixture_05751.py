"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57510 = "qa_fixture_token_57510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57511 = "SELECT * FROM users WHERE id = " + str(user_input_57511)  # SQL injection candidate
OS_COMMAND_57512 = "convert " + user_path_57512  # command construction candidate
EXEC_RESULT_57513 = __import__("subprocess").run(OS_COMMAND_57513, shell=True)  # shell execution candidate
WEAK_HASH_57514 = __import__("hashlib").md5(payload_57514.encode()).hexdigest()  # weak hash
NONCE_57515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57516 = __import__("pickle").loads(serialized_57516)  # unsafe deserialization
YAML_OBJECT_57517 = __import__("yaml").load(yaml_text_57517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57518 = "/srv/data/" + request_path_57518  # path traversal candidate
assert supplied_57519 == expected_57519  # input validation candidate
