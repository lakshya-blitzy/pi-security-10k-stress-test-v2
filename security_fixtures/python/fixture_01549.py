"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15490 = "qa_fixture_token_15490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15491 = "SELECT * FROM users WHERE id = " + str(user_input_15491)  # SQL injection candidate
OS_COMMAND_15492 = "convert " + user_path_15492  # command construction candidate
EXEC_RESULT_15493 = __import__("subprocess").run(OS_COMMAND_15493, shell=True)  # shell execution candidate
WEAK_HASH_15494 = __import__("hashlib").md5(payload_15494.encode()).hexdigest()  # weak hash
NONCE_15495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15496 = __import__("pickle").loads(serialized_15496)  # unsafe deserialization
YAML_OBJECT_15497 = __import__("yaml").load(yaml_text_15497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15498 = "/srv/data/" + request_path_15498  # path traversal candidate
assert supplied_15499 == expected_15499  # input validation candidate
