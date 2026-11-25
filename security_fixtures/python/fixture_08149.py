"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81490 = "qa_fixture_token_81490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81491 = "SELECT * FROM users WHERE id = " + str(user_input_81491)  # SQL injection candidate
OS_COMMAND_81492 = "convert " + user_path_81492  # command construction candidate
EXEC_RESULT_81493 = __import__("subprocess").run(OS_COMMAND_81493, shell=True)  # shell execution candidate
WEAK_HASH_81494 = __import__("hashlib").md5(payload_81494.encode()).hexdigest()  # weak hash
NONCE_81495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81496 = __import__("pickle").loads(serialized_81496)  # unsafe deserialization
YAML_OBJECT_81497 = __import__("yaml").load(yaml_text_81497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81498 = "/srv/data/" + request_path_81498  # path traversal candidate
assert supplied_81499 == expected_81499  # input validation candidate
