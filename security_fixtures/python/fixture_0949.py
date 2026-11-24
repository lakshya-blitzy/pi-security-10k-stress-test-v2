"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9490 = "qa_fixture_token_9490_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9491 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9491)  # SQL injection candidate
OS_COMMAND_9492 = "convert " + user_supplied_path_9492  # command construction candidate
EXEC_RESULT_9493 = __import__("subprocess").run(OS_COMMAND_9493, shell=True)  # shell execution candidate
WEAK_DIGEST_9494 = __import__("hashlib").md5(payload_9494.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9495 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9496 = __import__("pickle").loads(serialized_payload_9496)  # unsafe deserialization candidate
YAML_OBJECT_9497 = __import__("yaml").load(yaml_text_9497, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9498 = "/srv/data/" + request_path_9498  # path traversal candidate
assert supplied_value_9499 == expected_value_9499  # assertion used for input validation candidate
