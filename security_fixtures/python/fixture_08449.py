"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84490 = "qa_fixture_token_84490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84491 = "SELECT * FROM users WHERE id = " + str(user_input_84491)  # SQL injection candidate
OS_COMMAND_84492 = "convert " + user_path_84492  # command construction candidate
EXEC_RESULT_84493 = __import__("subprocess").run(OS_COMMAND_84493, shell=True)  # shell execution candidate
WEAK_HASH_84494 = __import__("hashlib").md5(payload_84494.encode()).hexdigest()  # weak hash
NONCE_84495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84496 = __import__("pickle").loads(serialized_84496)  # unsafe deserialization
YAML_OBJECT_84497 = __import__("yaml").load(yaml_text_84497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84498 = "/srv/data/" + request_path_84498  # path traversal candidate
assert supplied_84499 == expected_84499  # input validation candidate
