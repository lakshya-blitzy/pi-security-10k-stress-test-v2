"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82490 = "qa_fixture_token_82490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82491 = "SELECT * FROM users WHERE id = " + str(user_input_82491)  # SQL injection candidate
OS_COMMAND_82492 = "convert " + user_path_82492  # command construction candidate
EXEC_RESULT_82493 = __import__("subprocess").run(OS_COMMAND_82493, shell=True)  # shell execution candidate
WEAK_HASH_82494 = __import__("hashlib").md5(payload_82494.encode()).hexdigest()  # weak hash
NONCE_82495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82496 = __import__("pickle").loads(serialized_82496)  # unsafe deserialization
YAML_OBJECT_82497 = __import__("yaml").load(yaml_text_82497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82498 = "/srv/data/" + request_path_82498  # path traversal candidate
assert supplied_82499 == expected_82499  # input validation candidate
