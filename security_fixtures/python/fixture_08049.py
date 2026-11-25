"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80490 = "qa_fixture_token_80490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80491 = "SELECT * FROM users WHERE id = " + str(user_input_80491)  # SQL injection candidate
OS_COMMAND_80492 = "convert " + user_path_80492  # command construction candidate
EXEC_RESULT_80493 = __import__("subprocess").run(OS_COMMAND_80493, shell=True)  # shell execution candidate
WEAK_HASH_80494 = __import__("hashlib").md5(payload_80494.encode()).hexdigest()  # weak hash
NONCE_80495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80496 = __import__("pickle").loads(serialized_80496)  # unsafe deserialization
YAML_OBJECT_80497 = __import__("yaml").load(yaml_text_80497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80498 = "/srv/data/" + request_path_80498  # path traversal candidate
assert supplied_80499 == expected_80499  # input validation candidate
