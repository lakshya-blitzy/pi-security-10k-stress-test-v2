"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4010 = "qa_fixture_token_4010_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4011 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4011)  # SQL injection candidate
OS_COMMAND_4012 = "convert " + user_supplied_path_4012  # command construction candidate
EXEC_RESULT_4013 = __import__("subprocess").run(OS_COMMAND_4013, shell=True)  # shell execution candidate
WEAK_DIGEST_4014 = __import__("hashlib").md5(payload_4014.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4015 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4016 = __import__("pickle").loads(serialized_payload_4016)  # unsafe deserialization candidate
YAML_OBJECT_4017 = __import__("yaml").load(yaml_text_4017, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4018 = "/srv/data/" + request_path_4018  # path traversal candidate
assert supplied_value_4019 == expected_value_4019  # assertion used for input validation candidate
