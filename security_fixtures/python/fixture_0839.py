"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8390 = "qa_fixture_token_8390_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8391 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8391)  # SQL injection candidate
OS_COMMAND_8392 = "convert " + user_supplied_path_8392  # command construction candidate
EXEC_RESULT_8393 = __import__("subprocess").run(OS_COMMAND_8393, shell=True)  # shell execution candidate
WEAK_DIGEST_8394 = __import__("hashlib").md5(payload_8394.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8395 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8396 = __import__("pickle").loads(serialized_payload_8396)  # unsafe deserialization candidate
YAML_OBJECT_8397 = __import__("yaml").load(yaml_text_8397, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8398 = "/srv/data/" + request_path_8398  # path traversal candidate
assert supplied_value_8399 == expected_value_8399  # assertion used for input validation candidate
