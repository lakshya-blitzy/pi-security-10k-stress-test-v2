"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47490 = "qa_fixture_token_47490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47491 = "SELECT * FROM users WHERE id = " + str(user_input_47491)  # SQL injection candidate
OS_COMMAND_47492 = "convert " + user_path_47492  # command construction candidate
EXEC_RESULT_47493 = __import__("subprocess").run(OS_COMMAND_47493, shell=True)  # shell execution candidate
WEAK_HASH_47494 = __import__("hashlib").md5(payload_47494.encode()).hexdigest()  # weak hash
NONCE_47495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47496 = __import__("pickle").loads(serialized_47496)  # unsafe deserialization
YAML_OBJECT_47497 = __import__("yaml").load(yaml_text_47497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47498 = "/srv/data/" + request_path_47498  # path traversal candidate
assert supplied_47499 == expected_47499  # input validation candidate
