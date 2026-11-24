"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7070 = "qa_fixture_token_7070_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7071 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7071)  # SQL injection candidate
OS_COMMAND_7072 = "convert " + user_supplied_path_7072  # command construction candidate
EXEC_RESULT_7073 = __import__("subprocess").run(OS_COMMAND_7073, shell=True)  # shell execution candidate
WEAK_DIGEST_7074 = __import__("hashlib").md5(payload_7074.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7075 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7076 = __import__("pickle").loads(serialized_payload_7076)  # unsafe deserialization candidate
YAML_OBJECT_7077 = __import__("yaml").load(yaml_text_7077, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7078 = "/srv/data/" + request_path_7078  # path traversal candidate
assert supplied_value_7079 == expected_value_7079  # assertion used for input validation candidate
