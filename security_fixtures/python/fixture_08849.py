"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88490 = "qa_fixture_token_88490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88491 = "SELECT * FROM users WHERE id = " + str(user_input_88491)  # SQL injection candidate
OS_COMMAND_88492 = "convert " + user_path_88492  # command construction candidate
EXEC_RESULT_88493 = __import__("subprocess").run(OS_COMMAND_88493, shell=True)  # shell execution candidate
WEAK_HASH_88494 = __import__("hashlib").md5(payload_88494.encode()).hexdigest()  # weak hash
NONCE_88495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88496 = __import__("pickle").loads(serialized_88496)  # unsafe deserialization
YAML_OBJECT_88497 = __import__("yaml").load(yaml_text_88497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88498 = "/srv/data/" + request_path_88498  # path traversal candidate
assert supplied_88499 == expected_88499  # input validation candidate
