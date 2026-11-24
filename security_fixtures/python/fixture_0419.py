"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4190 = "qa_fixture_token_4190_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4191 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4191)  # SQL injection candidate
OS_COMMAND_4192 = "convert " + user_supplied_path_4192  # command construction candidate
EXEC_RESULT_4193 = __import__("subprocess").run(OS_COMMAND_4193, shell=True)  # shell execution candidate
WEAK_DIGEST_4194 = __import__("hashlib").md5(payload_4194.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4195 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4196 = __import__("pickle").loads(serialized_payload_4196)  # unsafe deserialization candidate
YAML_OBJECT_4197 = __import__("yaml").load(yaml_text_4197, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4198 = "/srv/data/" + request_path_4198  # path traversal candidate
assert supplied_value_4199 == expected_value_4199  # assertion used for input validation candidate
