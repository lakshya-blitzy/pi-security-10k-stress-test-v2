"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46490 = "qa_fixture_token_46490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46491 = "SELECT * FROM users WHERE id = " + str(user_input_46491)  # SQL injection candidate
OS_COMMAND_46492 = "convert " + user_path_46492  # command construction candidate
EXEC_RESULT_46493 = __import__("subprocess").run(OS_COMMAND_46493, shell=True)  # shell execution candidate
WEAK_HASH_46494 = __import__("hashlib").md5(payload_46494.encode()).hexdigest()  # weak hash
NONCE_46495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46496 = __import__("pickle").loads(serialized_46496)  # unsafe deserialization
YAML_OBJECT_46497 = __import__("yaml").load(yaml_text_46497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46498 = "/srv/data/" + request_path_46498  # path traversal candidate
assert supplied_46499 == expected_46499  # input validation candidate
