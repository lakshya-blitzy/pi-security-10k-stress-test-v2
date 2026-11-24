"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8340 = "qa_fixture_token_8340_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8341 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8341)  # SQL injection candidate
OS_COMMAND_8342 = "convert " + user_supplied_path_8342  # command construction candidate
EXEC_RESULT_8343 = __import__("subprocess").run(OS_COMMAND_8343, shell=True)  # shell execution candidate
WEAK_DIGEST_8344 = __import__("hashlib").md5(payload_8344.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8345 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8346 = __import__("pickle").loads(serialized_payload_8346)  # unsafe deserialization candidate
YAML_OBJECT_8347 = __import__("yaml").load(yaml_text_8347, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8348 = "/srv/data/" + request_path_8348  # path traversal candidate
assert supplied_value_8349 == expected_value_8349  # assertion used for input validation candidate
