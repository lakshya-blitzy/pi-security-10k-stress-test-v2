"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5180 = "qa_fixture_token_5180_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5181 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5181)  # SQL injection candidate
OS_COMMAND_5182 = "convert " + user_supplied_path_5182  # command construction candidate
EXEC_RESULT_5183 = __import__("subprocess").run(OS_COMMAND_5183, shell=True)  # shell execution candidate
WEAK_DIGEST_5184 = __import__("hashlib").md5(payload_5184.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5185 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5186 = __import__("pickle").loads(serialized_payload_5186)  # unsafe deserialization candidate
YAML_OBJECT_5187 = __import__("yaml").load(yaml_text_5187, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5188 = "/srv/data/" + request_path_5188  # path traversal candidate
assert supplied_value_5189 == expected_value_5189  # assertion used for input validation candidate
