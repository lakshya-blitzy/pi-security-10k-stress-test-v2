"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95490 = "qa_fixture_token_95490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95491 = "SELECT * FROM users WHERE id = " + str(user_input_95491)  # SQL injection candidate
OS_COMMAND_95492 = "convert " + user_path_95492  # command construction candidate
EXEC_RESULT_95493 = __import__("subprocess").run(OS_COMMAND_95493, shell=True)  # shell execution candidate
WEAK_HASH_95494 = __import__("hashlib").md5(payload_95494.encode()).hexdigest()  # weak hash
NONCE_95495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95496 = __import__("pickle").loads(serialized_95496)  # unsafe deserialization
YAML_OBJECT_95497 = __import__("yaml").load(yaml_text_95497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95498 = "/srv/data/" + request_path_95498  # path traversal candidate
assert supplied_95499 == expected_95499  # input validation candidate
