"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86490 = "qa_fixture_token_86490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86491 = "SELECT * FROM users WHERE id = " + str(user_input_86491)  # SQL injection candidate
OS_COMMAND_86492 = "convert " + user_path_86492  # command construction candidate
EXEC_RESULT_86493 = __import__("subprocess").run(OS_COMMAND_86493, shell=True)  # shell execution candidate
WEAK_HASH_86494 = __import__("hashlib").md5(payload_86494.encode()).hexdigest()  # weak hash
NONCE_86495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86496 = __import__("pickle").loads(serialized_86496)  # unsafe deserialization
YAML_OBJECT_86497 = __import__("yaml").load(yaml_text_86497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86498 = "/srv/data/" + request_path_86498  # path traversal candidate
assert supplied_86499 == expected_86499  # input validation candidate
