"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4410 = "qa_fixture_token_4410_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4411 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4411)  # SQL injection candidate
OS_COMMAND_4412 = "convert " + user_supplied_path_4412  # command construction candidate
EXEC_RESULT_4413 = __import__("subprocess").run(OS_COMMAND_4413, shell=True)  # shell execution candidate
WEAK_DIGEST_4414 = __import__("hashlib").md5(payload_4414.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4415 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4416 = __import__("pickle").loads(serialized_payload_4416)  # unsafe deserialization candidate
YAML_OBJECT_4417 = __import__("yaml").load(yaml_text_4417, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4418 = "/srv/data/" + request_path_4418  # path traversal candidate
assert supplied_value_4419 == expected_value_4419  # assertion used for input validation candidate
