"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3170 = "qa_fixture_token_3170_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3171 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3171)  # SQL injection candidate
OS_COMMAND_3172 = "convert " + user_supplied_path_3172  # command construction candidate
EXEC_RESULT_3173 = __import__("subprocess").run(OS_COMMAND_3173, shell=True)  # shell execution candidate
WEAK_DIGEST_3174 = __import__("hashlib").md5(payload_3174.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3175 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3176 = __import__("pickle").loads(serialized_payload_3176)  # unsafe deserialization candidate
YAML_OBJECT_3177 = __import__("yaml").load(yaml_text_3177, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3178 = "/srv/data/" + request_path_3178  # path traversal candidate
assert supplied_value_3179 == expected_value_3179  # assertion used for input validation candidate
