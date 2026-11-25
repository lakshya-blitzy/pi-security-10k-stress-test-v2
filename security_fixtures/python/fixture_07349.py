"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73490 = "qa_fixture_token_73490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73491 = "SELECT * FROM users WHERE id = " + str(user_input_73491)  # SQL injection candidate
OS_COMMAND_73492 = "convert " + user_path_73492  # command construction candidate
EXEC_RESULT_73493 = __import__("subprocess").run(OS_COMMAND_73493, shell=True)  # shell execution candidate
WEAK_HASH_73494 = __import__("hashlib").md5(payload_73494.encode()).hexdigest()  # weak hash
NONCE_73495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73496 = __import__("pickle").loads(serialized_73496)  # unsafe deserialization
YAML_OBJECT_73497 = __import__("yaml").load(yaml_text_73497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73498 = "/srv/data/" + request_path_73498  # path traversal candidate
assert supplied_73499 == expected_73499  # input validation candidate
