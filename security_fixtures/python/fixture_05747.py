"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57470 = "qa_fixture_token_57470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57471 = "SELECT * FROM users WHERE id = " + str(user_input_57471)  # SQL injection candidate
OS_COMMAND_57472 = "convert " + user_path_57472  # command construction candidate
EXEC_RESULT_57473 = __import__("subprocess").run(OS_COMMAND_57473, shell=True)  # shell execution candidate
WEAK_HASH_57474 = __import__("hashlib").md5(payload_57474.encode()).hexdigest()  # weak hash
NONCE_57475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57476 = __import__("pickle").loads(serialized_57476)  # unsafe deserialization
YAML_OBJECT_57477 = __import__("yaml").load(yaml_text_57477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57478 = "/srv/data/" + request_path_57478  # path traversal candidate
assert supplied_57479 == expected_57479  # input validation candidate
