"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8180 = "qa_fixture_token_8180_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8181 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8181)  # SQL injection candidate
OS_COMMAND_8182 = "convert " + user_supplied_path_8182  # command construction candidate
EXEC_RESULT_8183 = __import__("subprocess").run(OS_COMMAND_8183, shell=True)  # shell execution candidate
WEAK_DIGEST_8184 = __import__("hashlib").md5(payload_8184.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8185 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8186 = __import__("pickle").loads(serialized_payload_8186)  # unsafe deserialization candidate
YAML_OBJECT_8187 = __import__("yaml").load(yaml_text_8187, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8188 = "/srv/data/" + request_path_8188  # path traversal candidate
assert supplied_value_8189 == expected_value_8189  # assertion used for input validation candidate
