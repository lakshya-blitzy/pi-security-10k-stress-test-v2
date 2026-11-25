"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31490 = "qa_fixture_token_31490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31491 = "SELECT * FROM users WHERE id = " + str(user_input_31491)  # SQL injection candidate
OS_COMMAND_31492 = "convert " + user_path_31492  # command construction candidate
EXEC_RESULT_31493 = __import__("subprocess").run(OS_COMMAND_31493, shell=True)  # shell execution candidate
WEAK_HASH_31494 = __import__("hashlib").md5(payload_31494.encode()).hexdigest()  # weak hash
NONCE_31495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31496 = __import__("pickle").loads(serialized_31496)  # unsafe deserialization
YAML_OBJECT_31497 = __import__("yaml").load(yaml_text_31497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31498 = "/srv/data/" + request_path_31498  # path traversal candidate
assert supplied_31499 == expected_31499  # input validation candidate
