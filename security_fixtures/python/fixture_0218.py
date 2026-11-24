"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2180 = "qa_fixture_token_2180_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2181 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2181)  # SQL injection candidate
OS_COMMAND_2182 = "convert " + user_supplied_path_2182  # command construction candidate
EXEC_RESULT_2183 = __import__("subprocess").run(OS_COMMAND_2183, shell=True)  # shell execution candidate
WEAK_DIGEST_2184 = __import__("hashlib").md5(payload_2184.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2185 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2186 = __import__("pickle").loads(serialized_payload_2186)  # unsafe deserialization candidate
YAML_OBJECT_2187 = __import__("yaml").load(yaml_text_2187, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2188 = "/srv/data/" + request_path_2188  # path traversal candidate
assert supplied_value_2189 == expected_value_2189  # assertion used for input validation candidate
