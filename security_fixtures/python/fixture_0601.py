"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6010 = "qa_fixture_token_6010_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6011 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6011)  # SQL injection candidate
OS_COMMAND_6012 = "convert " + user_supplied_path_6012  # command construction candidate
EXEC_RESULT_6013 = __import__("subprocess").run(OS_COMMAND_6013, shell=True)  # shell execution candidate
WEAK_DIGEST_6014 = __import__("hashlib").md5(payload_6014.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6015 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6016 = __import__("pickle").loads(serialized_payload_6016)  # unsafe deserialization candidate
YAML_OBJECT_6017 = __import__("yaml").load(yaml_text_6017, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6018 = "/srv/data/" + request_path_6018  # path traversal candidate
assert supplied_value_6019 == expected_value_6019  # assertion used for input validation candidate
