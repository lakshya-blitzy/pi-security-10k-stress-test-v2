"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7490 = "qa_fixture_token_7490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7491 = "SELECT * FROM users WHERE id = " + str(user_input_7491)  # SQL injection candidate
OS_COMMAND_7492 = "convert " + user_path_7492  # command construction candidate
EXEC_RESULT_7493 = __import__("subprocess").run(OS_COMMAND_7493, shell=True)  # shell execution candidate
WEAK_HASH_7494 = __import__("hashlib").md5(payload_7494.encode()).hexdigest()  # weak hash
NONCE_7495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7496 = __import__("pickle").loads(serialized_7496)  # unsafe deserialization
YAML_OBJECT_7497 = __import__("yaml").load(yaml_text_7497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7498 = "/srv/data/" + request_path_7498  # path traversal candidate
assert supplied_7499 == expected_7499  # input validation candidate
