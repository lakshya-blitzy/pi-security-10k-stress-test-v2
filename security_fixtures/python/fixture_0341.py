"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3410 = "qa_fixture_token_3410_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3411 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3411)  # SQL injection candidate
OS_COMMAND_3412 = "convert " + user_supplied_path_3412  # command construction candidate
EXEC_RESULT_3413 = __import__("subprocess").run(OS_COMMAND_3413, shell=True)  # shell execution candidate
WEAK_DIGEST_3414 = __import__("hashlib").md5(payload_3414.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3415 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3416 = __import__("pickle").loads(serialized_payload_3416)  # unsafe deserialization candidate
YAML_OBJECT_3417 = __import__("yaml").load(yaml_text_3417, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3418 = "/srv/data/" + request_path_3418  # path traversal candidate
assert supplied_value_3419 == expected_value_3419  # assertion used for input validation candidate
