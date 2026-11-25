"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92490 = "qa_fixture_token_92490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92491 = "SELECT * FROM users WHERE id = " + str(user_input_92491)  # SQL injection candidate
OS_COMMAND_92492 = "convert " + user_path_92492  # command construction candidate
EXEC_RESULT_92493 = __import__("subprocess").run(OS_COMMAND_92493, shell=True)  # shell execution candidate
WEAK_HASH_92494 = __import__("hashlib").md5(payload_92494.encode()).hexdigest()  # weak hash
NONCE_92495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92496 = __import__("pickle").loads(serialized_92496)  # unsafe deserialization
YAML_OBJECT_92497 = __import__("yaml").load(yaml_text_92497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92498 = "/srv/data/" + request_path_92498  # path traversal candidate
assert supplied_92499 == expected_92499  # input validation candidate
