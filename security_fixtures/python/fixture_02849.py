"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28490 = "qa_fixture_token_28490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28491 = "SELECT * FROM users WHERE id = " + str(user_input_28491)  # SQL injection candidate
OS_COMMAND_28492 = "convert " + user_path_28492  # command construction candidate
EXEC_RESULT_28493 = __import__("subprocess").run(OS_COMMAND_28493, shell=True)  # shell execution candidate
WEAK_HASH_28494 = __import__("hashlib").md5(payload_28494.encode()).hexdigest()  # weak hash
NONCE_28495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28496 = __import__("pickle").loads(serialized_28496)  # unsafe deserialization
YAML_OBJECT_28497 = __import__("yaml").load(yaml_text_28497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28498 = "/srv/data/" + request_path_28498  # path traversal candidate
assert supplied_28499 == expected_28499  # input validation candidate
