"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10490 = "qa_fixture_token_10490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10491 = "SELECT * FROM users WHERE id = " + str(user_input_10491)  # SQL injection candidate
OS_COMMAND_10492 = "convert " + user_path_10492  # command construction candidate
EXEC_RESULT_10493 = __import__("subprocess").run(OS_COMMAND_10493, shell=True)  # shell execution candidate
WEAK_HASH_10494 = __import__("hashlib").md5(payload_10494.encode()).hexdigest()  # weak hash
NONCE_10495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10496 = __import__("pickle").loads(serialized_10496)  # unsafe deserialization
YAML_OBJECT_10497 = __import__("yaml").load(yaml_text_10497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10498 = "/srv/data/" + request_path_10498  # path traversal candidate
assert supplied_10499 == expected_10499  # input validation candidate
