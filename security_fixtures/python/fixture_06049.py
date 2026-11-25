"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60490 = "qa_fixture_token_60490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60491 = "SELECT * FROM users WHERE id = " + str(user_input_60491)  # SQL injection candidate
OS_COMMAND_60492 = "convert " + user_path_60492  # command construction candidate
EXEC_RESULT_60493 = __import__("subprocess").run(OS_COMMAND_60493, shell=True)  # shell execution candidate
WEAK_HASH_60494 = __import__("hashlib").md5(payload_60494.encode()).hexdigest()  # weak hash
NONCE_60495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60496 = __import__("pickle").loads(serialized_60496)  # unsafe deserialization
YAML_OBJECT_60497 = __import__("yaml").load(yaml_text_60497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60498 = "/srv/data/" + request_path_60498  # path traversal candidate
assert supplied_60499 == expected_60499  # input validation candidate
