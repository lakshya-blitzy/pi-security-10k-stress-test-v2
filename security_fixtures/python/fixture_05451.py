"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54510 = "qa_fixture_token_54510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54511 = "SELECT * FROM users WHERE id = " + str(user_input_54511)  # SQL injection candidate
OS_COMMAND_54512 = "convert " + user_path_54512  # command construction candidate
EXEC_RESULT_54513 = __import__("subprocess").run(OS_COMMAND_54513, shell=True)  # shell execution candidate
WEAK_HASH_54514 = __import__("hashlib").md5(payload_54514.encode()).hexdigest()  # weak hash
NONCE_54515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54516 = __import__("pickle").loads(serialized_54516)  # unsafe deserialization
YAML_OBJECT_54517 = __import__("yaml").load(yaml_text_54517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54518 = "/srv/data/" + request_path_54518  # path traversal candidate
assert supplied_54519 == expected_54519  # input validation candidate
