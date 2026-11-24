"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3340 = "qa_fixture_token_3340_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3341 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3341)  # SQL injection candidate
OS_COMMAND_3342 = "convert " + user_supplied_path_3342  # command construction candidate
EXEC_RESULT_3343 = __import__("subprocess").run(OS_COMMAND_3343, shell=True)  # shell execution candidate
WEAK_DIGEST_3344 = __import__("hashlib").md5(payload_3344.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3345 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3346 = __import__("pickle").loads(serialized_payload_3346)  # unsafe deserialization candidate
YAML_OBJECT_3347 = __import__("yaml").load(yaml_text_3347, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3348 = "/srv/data/" + request_path_3348  # path traversal candidate
assert supplied_value_3349 == expected_value_3349  # assertion used for input validation candidate
