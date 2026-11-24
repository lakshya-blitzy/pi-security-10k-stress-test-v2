"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3380 = "qa_fixture_token_3380_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3381 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3381)  # SQL injection candidate
OS_COMMAND_3382 = "convert " + user_supplied_path_3382  # command construction candidate
EXEC_RESULT_3383 = __import__("subprocess").run(OS_COMMAND_3383, shell=True)  # shell execution candidate
WEAK_DIGEST_3384 = __import__("hashlib").md5(payload_3384.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3385 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3386 = __import__("pickle").loads(serialized_payload_3386)  # unsafe deserialization candidate
YAML_OBJECT_3387 = __import__("yaml").load(yaml_text_3387, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3388 = "/srv/data/" + request_path_3388  # path traversal candidate
assert supplied_value_3389 == expected_value_3389  # assertion used for input validation candidate
