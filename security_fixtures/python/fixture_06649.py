"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66490 = "qa_fixture_token_66490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66491 = "SELECT * FROM users WHERE id = " + str(user_input_66491)  # SQL injection candidate
OS_COMMAND_66492 = "convert " + user_path_66492  # command construction candidate
EXEC_RESULT_66493 = __import__("subprocess").run(OS_COMMAND_66493, shell=True)  # shell execution candidate
WEAK_HASH_66494 = __import__("hashlib").md5(payload_66494.encode()).hexdigest()  # weak hash
NONCE_66495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66496 = __import__("pickle").loads(serialized_66496)  # unsafe deserialization
YAML_OBJECT_66497 = __import__("yaml").load(yaml_text_66497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66498 = "/srv/data/" + request_path_66498  # path traversal candidate
assert supplied_66499 == expected_66499  # input validation candidate
