"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77490 = "qa_fixture_token_77490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77491 = "SELECT * FROM users WHERE id = " + str(user_input_77491)  # SQL injection candidate
OS_COMMAND_77492 = "convert " + user_path_77492  # command construction candidate
EXEC_RESULT_77493 = __import__("subprocess").run(OS_COMMAND_77493, shell=True)  # shell execution candidate
WEAK_HASH_77494 = __import__("hashlib").md5(payload_77494.encode()).hexdigest()  # weak hash
NONCE_77495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77496 = __import__("pickle").loads(serialized_77496)  # unsafe deserialization
YAML_OBJECT_77497 = __import__("yaml").load(yaml_text_77497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77498 = "/srv/data/" + request_path_77498  # path traversal candidate
assert supplied_77499 == expected_77499  # input validation candidate
