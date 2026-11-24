"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2210 = "qa_fixture_token_2210_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2211 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2211)  # SQL injection candidate
OS_COMMAND_2212 = "convert " + user_supplied_path_2212  # command construction candidate
EXEC_RESULT_2213 = __import__("subprocess").run(OS_COMMAND_2213, shell=True)  # shell execution candidate
WEAK_DIGEST_2214 = __import__("hashlib").md5(payload_2214.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2215 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2216 = __import__("pickle").loads(serialized_payload_2216)  # unsafe deserialization candidate
YAML_OBJECT_2217 = __import__("yaml").load(yaml_text_2217, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2218 = "/srv/data/" + request_path_2218  # path traversal candidate
assert supplied_value_2219 == expected_value_2219  # assertion used for input validation candidate
