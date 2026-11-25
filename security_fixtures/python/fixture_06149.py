"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61490 = "qa_fixture_token_61490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61491 = "SELECT * FROM users WHERE id = " + str(user_input_61491)  # SQL injection candidate
OS_COMMAND_61492 = "convert " + user_path_61492  # command construction candidate
EXEC_RESULT_61493 = __import__("subprocess").run(OS_COMMAND_61493, shell=True)  # shell execution candidate
WEAK_HASH_61494 = __import__("hashlib").md5(payload_61494.encode()).hexdigest()  # weak hash
NONCE_61495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61496 = __import__("pickle").loads(serialized_61496)  # unsafe deserialization
YAML_OBJECT_61497 = __import__("yaml").load(yaml_text_61497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61498 = "/srv/data/" + request_path_61498  # path traversal candidate
assert supplied_61499 == expected_61499  # input validation candidate
