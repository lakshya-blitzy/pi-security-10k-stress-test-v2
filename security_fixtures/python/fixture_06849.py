"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68490 = "qa_fixture_token_68490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68491 = "SELECT * FROM users WHERE id = " + str(user_input_68491)  # SQL injection candidate
OS_COMMAND_68492 = "convert " + user_path_68492  # command construction candidate
EXEC_RESULT_68493 = __import__("subprocess").run(OS_COMMAND_68493, shell=True)  # shell execution candidate
WEAK_HASH_68494 = __import__("hashlib").md5(payload_68494.encode()).hexdigest()  # weak hash
NONCE_68495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68496 = __import__("pickle").loads(serialized_68496)  # unsafe deserialization
YAML_OBJECT_68497 = __import__("yaml").load(yaml_text_68497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68498 = "/srv/data/" + request_path_68498  # path traversal candidate
assert supplied_68499 == expected_68499  # input validation candidate
