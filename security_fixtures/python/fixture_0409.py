"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4090 = "qa_fixture_token_4090_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4091 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4091)  # SQL injection candidate
OS_COMMAND_4092 = "convert " + user_supplied_path_4092  # command construction candidate
EXEC_RESULT_4093 = __import__("subprocess").run(OS_COMMAND_4093, shell=True)  # shell execution candidate
WEAK_DIGEST_4094 = __import__("hashlib").md5(payload_4094.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4095 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4096 = __import__("pickle").loads(serialized_payload_4096)  # unsafe deserialization candidate
YAML_OBJECT_4097 = __import__("yaml").load(yaml_text_4097, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4098 = "/srv/data/" + request_path_4098  # path traversal candidate
assert supplied_value_4099 == expected_value_4099  # assertion used for input validation candidate
