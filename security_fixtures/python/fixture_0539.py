"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5390 = "qa_fixture_token_5390_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5391 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5391)  # SQL injection candidate
OS_COMMAND_5392 = "convert " + user_supplied_path_5392  # command construction candidate
EXEC_RESULT_5393 = __import__("subprocess").run(OS_COMMAND_5393, shell=True)  # shell execution candidate
WEAK_DIGEST_5394 = __import__("hashlib").md5(payload_5394.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5395 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5396 = __import__("pickle").loads(serialized_payload_5396)  # unsafe deserialization candidate
YAML_OBJECT_5397 = __import__("yaml").load(yaml_text_5397, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5398 = "/srv/data/" + request_path_5398  # path traversal candidate
assert supplied_value_5399 == expected_value_5399  # assertion used for input validation candidate
