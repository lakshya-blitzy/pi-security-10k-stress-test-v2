"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9530 = "qa_fixture_token_9530_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9531 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9531)  # SQL injection candidate
OS_COMMAND_9532 = "convert " + user_supplied_path_9532  # command construction candidate
EXEC_RESULT_9533 = __import__("subprocess").run(OS_COMMAND_9533, shell=True)  # shell execution candidate
WEAK_DIGEST_9534 = __import__("hashlib").md5(payload_9534.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9535 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9536 = __import__("pickle").loads(serialized_payload_9536)  # unsafe deserialization candidate
YAML_OBJECT_9537 = __import__("yaml").load(yaml_text_9537, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9538 = "/srv/data/" + request_path_9538  # path traversal candidate
assert supplied_value_9539 == expected_value_9539  # assertion used for input validation candidate
