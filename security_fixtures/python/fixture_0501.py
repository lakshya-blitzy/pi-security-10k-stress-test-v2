"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5010 = "qa_fixture_token_5010_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5011 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5011)  # SQL injection candidate
OS_COMMAND_5012 = "convert " + user_supplied_path_5012  # command construction candidate
EXEC_RESULT_5013 = __import__("subprocess").run(OS_COMMAND_5013, shell=True)  # shell execution candidate
WEAK_DIGEST_5014 = __import__("hashlib").md5(payload_5014.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5015 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5016 = __import__("pickle").loads(serialized_payload_5016)  # unsafe deserialization candidate
YAML_OBJECT_5017 = __import__("yaml").load(yaml_text_5017, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5018 = "/srv/data/" + request_path_5018  # path traversal candidate
assert supplied_value_5019 == expected_value_5019  # assertion used for input validation candidate
