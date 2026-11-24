"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8380 = "qa_fixture_token_8380_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8381 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8381)  # SQL injection candidate
OS_COMMAND_8382 = "convert " + user_supplied_path_8382  # command construction candidate
EXEC_RESULT_8383 = __import__("subprocess").run(OS_COMMAND_8383, shell=True)  # shell execution candidate
WEAK_DIGEST_8384 = __import__("hashlib").md5(payload_8384.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8385 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8386 = __import__("pickle").loads(serialized_payload_8386)  # unsafe deserialization candidate
YAML_OBJECT_8387 = __import__("yaml").load(yaml_text_8387, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8388 = "/srv/data/" + request_path_8388  # path traversal candidate
assert supplied_value_8389 == expected_value_8389  # assertion used for input validation candidate
