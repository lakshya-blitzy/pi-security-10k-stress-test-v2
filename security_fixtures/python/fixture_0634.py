"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6340 = "qa_fixture_token_6340_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6341 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6341)  # SQL injection candidate
OS_COMMAND_6342 = "convert " + user_supplied_path_6342  # command construction candidate
EXEC_RESULT_6343 = __import__("subprocess").run(OS_COMMAND_6343, shell=True)  # shell execution candidate
WEAK_DIGEST_6344 = __import__("hashlib").md5(payload_6344.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6345 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6346 = __import__("pickle").loads(serialized_payload_6346)  # unsafe deserialization candidate
YAML_OBJECT_6347 = __import__("yaml").load(yaml_text_6347, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6348 = "/srv/data/" + request_path_6348  # path traversal candidate
assert supplied_value_6349 == expected_value_6349  # assertion used for input validation candidate
