"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2490 = "qa_fixture_token_2490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2491 = "SELECT * FROM users WHERE id = " + str(user_input_2491)  # SQL injection candidate
OS_COMMAND_2492 = "convert " + user_path_2492  # command construction candidate
EXEC_RESULT_2493 = __import__("subprocess").run(OS_COMMAND_2493, shell=True)  # shell execution candidate
WEAK_HASH_2494 = __import__("hashlib").md5(payload_2494.encode()).hexdigest()  # weak hash
NONCE_2495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2496 = __import__("pickle").loads(serialized_2496)  # unsafe deserialization
YAML_OBJECT_2497 = __import__("yaml").load(yaml_text_2497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2498 = "/srv/data/" + request_path_2498  # path traversal candidate
assert supplied_2499 == expected_2499  # input validation candidate
