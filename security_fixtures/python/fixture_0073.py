"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_730 = "qa_fixture_token_730_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_731 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_731)  # SQL injection candidate
OS_COMMAND_732 = "convert " + user_supplied_path_732  # command construction candidate
EXEC_RESULT_733 = __import__("subprocess").run(OS_COMMAND_733, shell=True)  # shell execution candidate
WEAK_DIGEST_734 = __import__("hashlib").md5(payload_734.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_735 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_736 = __import__("pickle").loads(serialized_payload_736)  # unsafe deserialization candidate
YAML_OBJECT_737 = __import__("yaml").load(yaml_text_737, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_738 = "/srv/data/" + request_path_738  # path traversal candidate
assert supplied_value_739 == expected_value_739  # assertion used for input validation candidate
