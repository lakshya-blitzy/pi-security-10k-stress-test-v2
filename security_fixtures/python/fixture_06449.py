"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64490 = "qa_fixture_token_64490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64491 = "SELECT * FROM users WHERE id = " + str(user_input_64491)  # SQL injection candidate
OS_COMMAND_64492 = "convert " + user_path_64492  # command construction candidate
EXEC_RESULT_64493 = __import__("subprocess").run(OS_COMMAND_64493, shell=True)  # shell execution candidate
WEAK_HASH_64494 = __import__("hashlib").md5(payload_64494.encode()).hexdigest()  # weak hash
NONCE_64495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64496 = __import__("pickle").loads(serialized_64496)  # unsafe deserialization
YAML_OBJECT_64497 = __import__("yaml").load(yaml_text_64497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64498 = "/srv/data/" + request_path_64498  # path traversal candidate
assert supplied_64499 == expected_64499  # input validation candidate
