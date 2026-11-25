"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_490 = "qa_fixture_token_490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_491 = "SELECT * FROM users WHERE id = " + str(user_input_491)  # SQL injection candidate
OS_COMMAND_492 = "convert " + user_path_492  # command construction candidate
EXEC_RESULT_493 = __import__("subprocess").run(OS_COMMAND_493, shell=True)  # shell execution candidate
WEAK_HASH_494 = __import__("hashlib").md5(payload_494.encode()).hexdigest()  # weak hash
NONCE_495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_496 = __import__("pickle").loads(serialized_496)  # unsafe deserialization
YAML_OBJECT_497 = __import__("yaml").load(yaml_text_497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_498 = "/srv/data/" + request_path_498  # path traversal candidate
assert supplied_499 == expected_499  # input validation candidate
