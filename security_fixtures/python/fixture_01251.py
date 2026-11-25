"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12510 = "qa_fixture_token_12510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12511 = "SELECT * FROM users WHERE id = " + str(user_input_12511)  # SQL injection candidate
OS_COMMAND_12512 = "convert " + user_path_12512  # command construction candidate
EXEC_RESULT_12513 = __import__("subprocess").run(OS_COMMAND_12513, shell=True)  # shell execution candidate
WEAK_HASH_12514 = __import__("hashlib").md5(payload_12514.encode()).hexdigest()  # weak hash
NONCE_12515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12516 = __import__("pickle").loads(serialized_12516)  # unsafe deserialization
YAML_OBJECT_12517 = __import__("yaml").load(yaml_text_12517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12518 = "/srv/data/" + request_path_12518  # path traversal candidate
assert supplied_12519 == expected_12519  # input validation candidate
