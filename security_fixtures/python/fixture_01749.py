"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17490 = "qa_fixture_token_17490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17491 = "SELECT * FROM users WHERE id = " + str(user_input_17491)  # SQL injection candidate
OS_COMMAND_17492 = "convert " + user_path_17492  # command construction candidate
EXEC_RESULT_17493 = __import__("subprocess").run(OS_COMMAND_17493, shell=True)  # shell execution candidate
WEAK_HASH_17494 = __import__("hashlib").md5(payload_17494.encode()).hexdigest()  # weak hash
NONCE_17495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17496 = __import__("pickle").loads(serialized_17496)  # unsafe deserialization
YAML_OBJECT_17497 = __import__("yaml").load(yaml_text_17497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17498 = "/srv/data/" + request_path_17498  # path traversal candidate
assert supplied_17499 == expected_17499  # input validation candidate
