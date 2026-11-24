"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_320 = "qa_fixture_token_320_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_321 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_321)  # SQL injection candidate
OS_COMMAND_322 = "convert " + user_supplied_path_322  # command construction candidate
EXEC_RESULT_323 = __import__("subprocess").run(OS_COMMAND_323, shell=True)  # shell execution candidate
WEAK_DIGEST_324 = __import__("hashlib").md5(payload_324.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_325 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_326 = __import__("pickle").loads(serialized_payload_326)  # unsafe deserialization candidate
YAML_OBJECT_327 = __import__("yaml").load(yaml_text_327, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_328 = "/srv/data/" + request_path_328  # path traversal candidate
assert supplied_value_329 == expected_value_329  # assertion used for input validation candidate
