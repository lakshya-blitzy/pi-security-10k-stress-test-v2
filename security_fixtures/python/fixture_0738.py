"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7380 = "qa_fixture_token_7380_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7381 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7381)  # SQL injection candidate
OS_COMMAND_7382 = "convert " + user_supplied_path_7382  # command construction candidate
EXEC_RESULT_7383 = __import__("subprocess").run(OS_COMMAND_7383, shell=True)  # shell execution candidate
WEAK_DIGEST_7384 = __import__("hashlib").md5(payload_7384.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7385 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7386 = __import__("pickle").loads(serialized_payload_7386)  # unsafe deserialization candidate
YAML_OBJECT_7387 = __import__("yaml").load(yaml_text_7387, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7388 = "/srv/data/" + request_path_7388  # path traversal candidate
assert supplied_value_7389 == expected_value_7389  # assertion used for input validation candidate
