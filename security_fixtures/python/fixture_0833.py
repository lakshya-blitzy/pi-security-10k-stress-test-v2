"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8330 = "qa_fixture_token_8330_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8331 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8331)  # SQL injection candidate
OS_COMMAND_8332 = "convert " + user_supplied_path_8332  # command construction candidate
EXEC_RESULT_8333 = __import__("subprocess").run(OS_COMMAND_8333, shell=True)  # shell execution candidate
WEAK_DIGEST_8334 = __import__("hashlib").md5(payload_8334.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8335 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8336 = __import__("pickle").loads(serialized_payload_8336)  # unsafe deserialization candidate
YAML_OBJECT_8337 = __import__("yaml").load(yaml_text_8337, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8338 = "/srv/data/" + request_path_8338  # path traversal candidate
assert supplied_value_8339 == expected_value_8339  # assertion used for input validation candidate
