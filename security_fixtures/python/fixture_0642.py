"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6420 = "qa_fixture_token_6420_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6421 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6421)  # SQL injection candidate
OS_COMMAND_6422 = "convert " + user_supplied_path_6422  # command construction candidate
EXEC_RESULT_6423 = __import__("subprocess").run(OS_COMMAND_6423, shell=True)  # shell execution candidate
WEAK_DIGEST_6424 = __import__("hashlib").md5(payload_6424.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6425 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6426 = __import__("pickle").loads(serialized_payload_6426)  # unsafe deserialization candidate
YAML_OBJECT_6427 = __import__("yaml").load(yaml_text_6427, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6428 = "/srv/data/" + request_path_6428  # path traversal candidate
assert supplied_value_6429 == expected_value_6429  # assertion used for input validation candidate
