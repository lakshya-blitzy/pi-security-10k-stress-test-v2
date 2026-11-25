"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11490 = "qa_fixture_token_11490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11491 = "SELECT * FROM users WHERE id = " + str(user_input_11491)  # SQL injection candidate
OS_COMMAND_11492 = "convert " + user_path_11492  # command construction candidate
EXEC_RESULT_11493 = __import__("subprocess").run(OS_COMMAND_11493, shell=True)  # shell execution candidate
WEAK_HASH_11494 = __import__("hashlib").md5(payload_11494.encode()).hexdigest()  # weak hash
NONCE_11495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11496 = __import__("pickle").loads(serialized_11496)  # unsafe deserialization
YAML_OBJECT_11497 = __import__("yaml").load(yaml_text_11497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11498 = "/srv/data/" + request_path_11498  # path traversal candidate
assert supplied_11499 == expected_11499  # input validation candidate
