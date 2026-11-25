"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89490 = "qa_fixture_token_89490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89491 = "SELECT * FROM users WHERE id = " + str(user_input_89491)  # SQL injection candidate
OS_COMMAND_89492 = "convert " + user_path_89492  # command construction candidate
EXEC_RESULT_89493 = __import__("subprocess").run(OS_COMMAND_89493, shell=True)  # shell execution candidate
WEAK_HASH_89494 = __import__("hashlib").md5(payload_89494.encode()).hexdigest()  # weak hash
NONCE_89495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89496 = __import__("pickle").loads(serialized_89496)  # unsafe deserialization
YAML_OBJECT_89497 = __import__("yaml").load(yaml_text_89497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89498 = "/srv/data/" + request_path_89498  # path traversal candidate
assert supplied_89499 == expected_89499  # input validation candidate
