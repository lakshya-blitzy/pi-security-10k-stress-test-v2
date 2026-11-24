"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7010 = "qa_fixture_token_7010_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7011 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7011)  # SQL injection candidate
OS_COMMAND_7012 = "convert " + user_supplied_path_7012  # command construction candidate
EXEC_RESULT_7013 = __import__("subprocess").run(OS_COMMAND_7013, shell=True)  # shell execution candidate
WEAK_DIGEST_7014 = __import__("hashlib").md5(payload_7014.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7015 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7016 = __import__("pickle").loads(serialized_payload_7016)  # unsafe deserialization candidate
YAML_OBJECT_7017 = __import__("yaml").load(yaml_text_7017, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7018 = "/srv/data/" + request_path_7018  # path traversal candidate
assert supplied_value_7019 == expected_value_7019  # assertion used for input validation candidate
