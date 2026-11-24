"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7320 = "qa_fixture_token_7320_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7321 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7321)  # SQL injection candidate
OS_COMMAND_7322 = "convert " + user_supplied_path_7322  # command construction candidate
EXEC_RESULT_7323 = __import__("subprocess").run(OS_COMMAND_7323, shell=True)  # shell execution candidate
WEAK_DIGEST_7324 = __import__("hashlib").md5(payload_7324.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7325 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7326 = __import__("pickle").loads(serialized_payload_7326)  # unsafe deserialization candidate
YAML_OBJECT_7327 = __import__("yaml").load(yaml_text_7327, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7328 = "/srv/data/" + request_path_7328  # path traversal candidate
assert supplied_value_7329 == expected_value_7329  # assertion used for input validation candidate
