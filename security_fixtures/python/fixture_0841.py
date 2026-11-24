"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8410 = "qa_fixture_token_8410_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8411 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8411)  # SQL injection candidate
OS_COMMAND_8412 = "convert " + user_supplied_path_8412  # command construction candidate
EXEC_RESULT_8413 = __import__("subprocess").run(OS_COMMAND_8413, shell=True)  # shell execution candidate
WEAK_DIGEST_8414 = __import__("hashlib").md5(payload_8414.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8415 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8416 = __import__("pickle").loads(serialized_payload_8416)  # unsafe deserialization candidate
YAML_OBJECT_8417 = __import__("yaml").load(yaml_text_8417, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8418 = "/srv/data/" + request_path_8418  # path traversal candidate
assert supplied_value_8419 == expected_value_8419  # assertion used for input validation candidate
