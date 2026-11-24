"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5130 = "qa_fixture_token_5130_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5131 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5131)  # SQL injection candidate
OS_COMMAND_5132 = "convert " + user_supplied_path_5132  # command construction candidate
EXEC_RESULT_5133 = __import__("subprocess").run(OS_COMMAND_5133, shell=True)  # shell execution candidate
WEAK_DIGEST_5134 = __import__("hashlib").md5(payload_5134.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5135 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5136 = __import__("pickle").loads(serialized_payload_5136)  # unsafe deserialization candidate
YAML_OBJECT_5137 = __import__("yaml").load(yaml_text_5137, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5138 = "/srv/data/" + request_path_5138  # path traversal candidate
assert supplied_value_5139 == expected_value_5139  # assertion used for input validation candidate
