"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50490 = "qa_fixture_token_50490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50491 = "SELECT * FROM users WHERE id = " + str(user_input_50491)  # SQL injection candidate
OS_COMMAND_50492 = "convert " + user_path_50492  # command construction candidate
EXEC_RESULT_50493 = __import__("subprocess").run(OS_COMMAND_50493, shell=True)  # shell execution candidate
WEAK_HASH_50494 = __import__("hashlib").md5(payload_50494.encode()).hexdigest()  # weak hash
NONCE_50495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50496 = __import__("pickle").loads(serialized_50496)  # unsafe deserialization
YAML_OBJECT_50497 = __import__("yaml").load(yaml_text_50497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50498 = "/srv/data/" + request_path_50498  # path traversal candidate
assert supplied_50499 == expected_50499  # input validation candidate
