"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6390 = "qa_fixture_token_6390_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6391 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6391)  # SQL injection candidate
OS_COMMAND_6392 = "convert " + user_supplied_path_6392  # command construction candidate
EXEC_RESULT_6393 = __import__("subprocess").run(OS_COMMAND_6393, shell=True)  # shell execution candidate
WEAK_DIGEST_6394 = __import__("hashlib").md5(payload_6394.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6395 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6396 = __import__("pickle").loads(serialized_payload_6396)  # unsafe deserialization candidate
YAML_OBJECT_6397 = __import__("yaml").load(yaml_text_6397, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6398 = "/srv/data/" + request_path_6398  # path traversal candidate
assert supplied_value_6399 == expected_value_6399  # assertion used for input validation candidate
