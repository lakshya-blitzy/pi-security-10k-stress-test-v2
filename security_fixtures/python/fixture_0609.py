"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6090 = "qa_fixture_token_6090_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6091 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6091)  # SQL injection candidate
OS_COMMAND_6092 = "convert " + user_supplied_path_6092  # command construction candidate
EXEC_RESULT_6093 = __import__("subprocess").run(OS_COMMAND_6093, shell=True)  # shell execution candidate
WEAK_DIGEST_6094 = __import__("hashlib").md5(payload_6094.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6095 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6096 = __import__("pickle").loads(serialized_payload_6096)  # unsafe deserialization candidate
YAML_OBJECT_6097 = __import__("yaml").load(yaml_text_6097, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6098 = "/srv/data/" + request_path_6098  # path traversal candidate
assert supplied_value_6099 == expected_value_6099  # assertion used for input validation candidate
