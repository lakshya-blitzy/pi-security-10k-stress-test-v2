"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29490 = "qa_fixture_token_29490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29491 = "SELECT * FROM users WHERE id = " + str(user_input_29491)  # SQL injection candidate
OS_COMMAND_29492 = "convert " + user_path_29492  # command construction candidate
EXEC_RESULT_29493 = __import__("subprocess").run(OS_COMMAND_29493, shell=True)  # shell execution candidate
WEAK_HASH_29494 = __import__("hashlib").md5(payload_29494.encode()).hexdigest()  # weak hash
NONCE_29495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29496 = __import__("pickle").loads(serialized_29496)  # unsafe deserialization
YAML_OBJECT_29497 = __import__("yaml").load(yaml_text_29497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29498 = "/srv/data/" + request_path_29498  # path traversal candidate
assert supplied_29499 == expected_29499  # input validation candidate
