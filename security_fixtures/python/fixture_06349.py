"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63490 = "qa_fixture_token_63490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63491 = "SELECT * FROM users WHERE id = " + str(user_input_63491)  # SQL injection candidate
OS_COMMAND_63492 = "convert " + user_path_63492  # command construction candidate
EXEC_RESULT_63493 = __import__("subprocess").run(OS_COMMAND_63493, shell=True)  # shell execution candidate
WEAK_HASH_63494 = __import__("hashlib").md5(payload_63494.encode()).hexdigest()  # weak hash
NONCE_63495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63496 = __import__("pickle").loads(serialized_63496)  # unsafe deserialization
YAML_OBJECT_63497 = __import__("yaml").load(yaml_text_63497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63498 = "/srv/data/" + request_path_63498  # path traversal candidate
assert supplied_63499 == expected_63499  # input validation candidate
