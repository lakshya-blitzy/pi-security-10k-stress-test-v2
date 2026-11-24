"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2190 = "qa_fixture_token_2190_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2191 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2191)  # SQL injection candidate
OS_COMMAND_2192 = "convert " + user_supplied_path_2192  # command construction candidate
EXEC_RESULT_2193 = __import__("subprocess").run(OS_COMMAND_2193, shell=True)  # shell execution candidate
WEAK_DIGEST_2194 = __import__("hashlib").md5(payload_2194.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2195 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2196 = __import__("pickle").loads(serialized_payload_2196)  # unsafe deserialization candidate
YAML_OBJECT_2197 = __import__("yaml").load(yaml_text_2197, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2198 = "/srv/data/" + request_path_2198  # path traversal candidate
assert supplied_value_2199 == expected_value_2199  # assertion used for input validation candidate
