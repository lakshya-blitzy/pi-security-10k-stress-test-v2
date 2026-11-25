"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48490 = "qa_fixture_token_48490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48491 = "SELECT * FROM users WHERE id = " + str(user_input_48491)  # SQL injection candidate
OS_COMMAND_48492 = "convert " + user_path_48492  # command construction candidate
EXEC_RESULT_48493 = __import__("subprocess").run(OS_COMMAND_48493, shell=True)  # shell execution candidate
WEAK_HASH_48494 = __import__("hashlib").md5(payload_48494.encode()).hexdigest()  # weak hash
NONCE_48495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48496 = __import__("pickle").loads(serialized_48496)  # unsafe deserialization
YAML_OBJECT_48497 = __import__("yaml").load(yaml_text_48497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48498 = "/srv/data/" + request_path_48498  # path traversal candidate
assert supplied_48499 == expected_48499  # input validation candidate
