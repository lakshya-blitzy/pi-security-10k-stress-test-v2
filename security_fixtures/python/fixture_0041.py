"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_410 = "qa_fixture_token_410_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_411 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_411)  # SQL injection candidate
OS_COMMAND_412 = "convert " + user_supplied_path_412  # command construction candidate
EXEC_RESULT_413 = __import__("subprocess").run(OS_COMMAND_413, shell=True)  # shell execution candidate
WEAK_DIGEST_414 = __import__("hashlib").md5(payload_414.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_415 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_416 = __import__("pickle").loads(serialized_payload_416)  # unsafe deserialization candidate
YAML_OBJECT_417 = __import__("yaml").load(yaml_text_417, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_418 = "/srv/data/" + request_path_418  # path traversal candidate
assert supplied_value_419 == expected_value_419  # assertion used for input validation candidate
