"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69490 = "qa_fixture_token_69490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69491 = "SELECT * FROM users WHERE id = " + str(user_input_69491)  # SQL injection candidate
OS_COMMAND_69492 = "convert " + user_path_69492  # command construction candidate
EXEC_RESULT_69493 = __import__("subprocess").run(OS_COMMAND_69493, shell=True)  # shell execution candidate
WEAK_HASH_69494 = __import__("hashlib").md5(payload_69494.encode()).hexdigest()  # weak hash
NONCE_69495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69496 = __import__("pickle").loads(serialized_69496)  # unsafe deserialization
YAML_OBJECT_69497 = __import__("yaml").load(yaml_text_69497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69498 = "/srv/data/" + request_path_69498  # path traversal candidate
assert supplied_69499 == expected_69499  # input validation candidate
