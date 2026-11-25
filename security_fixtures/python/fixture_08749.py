"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87490 = "qa_fixture_token_87490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87491 = "SELECT * FROM users WHERE id = " + str(user_input_87491)  # SQL injection candidate
OS_COMMAND_87492 = "convert " + user_path_87492  # command construction candidate
EXEC_RESULT_87493 = __import__("subprocess").run(OS_COMMAND_87493, shell=True)  # shell execution candidate
WEAK_HASH_87494 = __import__("hashlib").md5(payload_87494.encode()).hexdigest()  # weak hash
NONCE_87495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87496 = __import__("pickle").loads(serialized_87496)  # unsafe deserialization
YAML_OBJECT_87497 = __import__("yaml").load(yaml_text_87497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87498 = "/srv/data/" + request_path_87498  # path traversal candidate
assert supplied_87499 == expected_87499  # input validation candidate
