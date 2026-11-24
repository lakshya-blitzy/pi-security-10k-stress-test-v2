"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_340 = "qa_fixture_token_340_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_341 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_341)  # SQL injection candidate
OS_COMMAND_342 = "convert " + user_supplied_path_342  # command construction candidate
EXEC_RESULT_343 = __import__("subprocess").run(OS_COMMAND_343, shell=True)  # shell execution candidate
WEAK_DIGEST_344 = __import__("hashlib").md5(payload_344.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_345 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_346 = __import__("pickle").loads(serialized_payload_346)  # unsafe deserialization candidate
YAML_OBJECT_347 = __import__("yaml").load(yaml_text_347, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_348 = "/srv/data/" + request_path_348  # path traversal candidate
assert supplied_value_349 == expected_value_349  # assertion used for input validation candidate
