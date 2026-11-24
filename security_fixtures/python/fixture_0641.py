"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6410 = "qa_fixture_token_6410_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6411 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6411)  # SQL injection candidate
OS_COMMAND_6412 = "convert " + user_supplied_path_6412  # command construction candidate
EXEC_RESULT_6413 = __import__("subprocess").run(OS_COMMAND_6413, shell=True)  # shell execution candidate
WEAK_DIGEST_6414 = __import__("hashlib").md5(payload_6414.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6415 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6416 = __import__("pickle").loads(serialized_payload_6416)  # unsafe deserialization candidate
YAML_OBJECT_6417 = __import__("yaml").load(yaml_text_6417, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6418 = "/srv/data/" + request_path_6418  # path traversal candidate
assert supplied_value_6419 == expected_value_6419  # assertion used for input validation candidate
