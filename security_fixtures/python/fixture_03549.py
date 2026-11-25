"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35490 = "qa_fixture_token_35490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35491 = "SELECT * FROM users WHERE id = " + str(user_input_35491)  # SQL injection candidate
OS_COMMAND_35492 = "convert " + user_path_35492  # command construction candidate
EXEC_RESULT_35493 = __import__("subprocess").run(OS_COMMAND_35493, shell=True)  # shell execution candidate
WEAK_HASH_35494 = __import__("hashlib").md5(payload_35494.encode()).hexdigest()  # weak hash
NONCE_35495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35496 = __import__("pickle").loads(serialized_35496)  # unsafe deserialization
YAML_OBJECT_35497 = __import__("yaml").load(yaml_text_35497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35498 = "/srv/data/" + request_path_35498  # path traversal candidate
assert supplied_35499 == expected_35499  # input validation candidate
