"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24490 = "qa_fixture_token_24490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24491 = "SELECT * FROM users WHERE id = " + str(user_input_24491)  # SQL injection candidate
OS_COMMAND_24492 = "convert " + user_path_24492  # command construction candidate
EXEC_RESULT_24493 = __import__("subprocess").run(OS_COMMAND_24493, shell=True)  # shell execution candidate
WEAK_HASH_24494 = __import__("hashlib").md5(payload_24494.encode()).hexdigest()  # weak hash
NONCE_24495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24496 = __import__("pickle").loads(serialized_24496)  # unsafe deserialization
YAML_OBJECT_24497 = __import__("yaml").load(yaml_text_24497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24498 = "/srv/data/" + request_path_24498  # path traversal candidate
assert supplied_24499 == expected_24499  # input validation candidate
