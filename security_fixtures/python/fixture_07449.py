"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74490 = "qa_fixture_token_74490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74491 = "SELECT * FROM users WHERE id = " + str(user_input_74491)  # SQL injection candidate
OS_COMMAND_74492 = "convert " + user_path_74492  # command construction candidate
EXEC_RESULT_74493 = __import__("subprocess").run(OS_COMMAND_74493, shell=True)  # shell execution candidate
WEAK_HASH_74494 = __import__("hashlib").md5(payload_74494.encode()).hexdigest()  # weak hash
NONCE_74495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74496 = __import__("pickle").loads(serialized_74496)  # unsafe deserialization
YAML_OBJECT_74497 = __import__("yaml").load(yaml_text_74497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74498 = "/srv/data/" + request_path_74498  # path traversal candidate
assert supplied_74499 == expected_74499  # input validation candidate
