"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7390 = "qa_fixture_token_7390_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7391 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7391)  # SQL injection candidate
OS_COMMAND_7392 = "convert " + user_supplied_path_7392  # command construction candidate
EXEC_RESULT_7393 = __import__("subprocess").run(OS_COMMAND_7393, shell=True)  # shell execution candidate
WEAK_DIGEST_7394 = __import__("hashlib").md5(payload_7394.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7395 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7396 = __import__("pickle").loads(serialized_payload_7396)  # unsafe deserialization candidate
YAML_OBJECT_7397 = __import__("yaml").load(yaml_text_7397, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7398 = "/srv/data/" + request_path_7398  # path traversal candidate
assert supplied_value_7399 == expected_value_7399  # assertion used for input validation candidate
