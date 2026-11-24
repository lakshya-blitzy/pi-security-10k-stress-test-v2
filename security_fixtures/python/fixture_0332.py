"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3320 = "qa_fixture_token_3320_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3321 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3321)  # SQL injection candidate
OS_COMMAND_3322 = "convert " + user_supplied_path_3322  # command construction candidate
EXEC_RESULT_3323 = __import__("subprocess").run(OS_COMMAND_3323, shell=True)  # shell execution candidate
WEAK_DIGEST_3324 = __import__("hashlib").md5(payload_3324.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3325 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3326 = __import__("pickle").loads(serialized_payload_3326)  # unsafe deserialization candidate
YAML_OBJECT_3327 = __import__("yaml").load(yaml_text_3327, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3328 = "/srv/data/" + request_path_3328  # path traversal candidate
assert supplied_value_3329 == expected_value_3329  # assertion used for input validation candidate
