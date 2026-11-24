"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3390 = "qa_fixture_token_3390_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3391 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3391)  # SQL injection candidate
OS_COMMAND_3392 = "convert " + user_supplied_path_3392  # command construction candidate
EXEC_RESULT_3393 = __import__("subprocess").run(OS_COMMAND_3393, shell=True)  # shell execution candidate
WEAK_DIGEST_3394 = __import__("hashlib").md5(payload_3394.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3395 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3396 = __import__("pickle").loads(serialized_payload_3396)  # unsafe deserialization candidate
YAML_OBJECT_3397 = __import__("yaml").load(yaml_text_3397, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3398 = "/srv/data/" + request_path_3398  # path traversal candidate
assert supplied_value_3399 == expected_value_3399  # assertion used for input validation candidate
