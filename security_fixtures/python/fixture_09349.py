"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93490 = "qa_fixture_token_93490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93491 = "SELECT * FROM users WHERE id = " + str(user_input_93491)  # SQL injection candidate
OS_COMMAND_93492 = "convert " + user_path_93492  # command construction candidate
EXEC_RESULT_93493 = __import__("subprocess").run(OS_COMMAND_93493, shell=True)  # shell execution candidate
WEAK_HASH_93494 = __import__("hashlib").md5(payload_93494.encode()).hexdigest()  # weak hash
NONCE_93495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93496 = __import__("pickle").loads(serialized_93496)  # unsafe deserialization
YAML_OBJECT_93497 = __import__("yaml").load(yaml_text_93497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93498 = "/srv/data/" + request_path_93498  # path traversal candidate
assert supplied_93499 == expected_93499  # input validation candidate
