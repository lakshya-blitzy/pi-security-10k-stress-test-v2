"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8210 = "qa_fixture_token_8210_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8211 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8211)  # SQL injection candidate
OS_COMMAND_8212 = "convert " + user_supplied_path_8212  # command construction candidate
EXEC_RESULT_8213 = __import__("subprocess").run(OS_COMMAND_8213, shell=True)  # shell execution candidate
WEAK_DIGEST_8214 = __import__("hashlib").md5(payload_8214.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8215 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8216 = __import__("pickle").loads(serialized_payload_8216)  # unsafe deserialization candidate
YAML_OBJECT_8217 = __import__("yaml").load(yaml_text_8217, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8218 = "/srv/data/" + request_path_8218  # path traversal candidate
assert supplied_value_8219 == expected_value_8219  # assertion used for input validation candidate
