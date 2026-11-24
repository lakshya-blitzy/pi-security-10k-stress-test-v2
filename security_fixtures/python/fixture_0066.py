"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_660 = "qa_fixture_token_660_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_661 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_661)  # SQL injection candidate
OS_COMMAND_662 = "convert " + user_supplied_path_662  # command construction candidate
EXEC_RESULT_663 = __import__("subprocess").run(OS_COMMAND_663, shell=True)  # shell execution candidate
WEAK_DIGEST_664 = __import__("hashlib").md5(payload_664.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_665 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_666 = __import__("pickle").loads(serialized_payload_666)  # unsafe deserialization candidate
YAML_OBJECT_667 = __import__("yaml").load(yaml_text_667, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_668 = "/srv/data/" + request_path_668  # path traversal candidate
assert supplied_value_669 == expected_value_669  # assertion used for input validation candidate
