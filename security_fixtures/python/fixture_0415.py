"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4150 = "qa_fixture_token_4150_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4151 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4151)  # SQL injection candidate
OS_COMMAND_4152 = "convert " + user_supplied_path_4152  # command construction candidate
EXEC_RESULT_4153 = __import__("subprocess").run(OS_COMMAND_4153, shell=True)  # shell execution candidate
WEAK_DIGEST_4154 = __import__("hashlib").md5(payload_4154.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4155 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4156 = __import__("pickle").loads(serialized_payload_4156)  # unsafe deserialization candidate
YAML_OBJECT_4157 = __import__("yaml").load(yaml_text_4157, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4158 = "/srv/data/" + request_path_4158  # path traversal candidate
assert supplied_value_4159 == expected_value_4159  # assertion used for input validation candidate
