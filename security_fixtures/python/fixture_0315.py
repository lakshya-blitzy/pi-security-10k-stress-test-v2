"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3150 = "qa_fixture_token_3150_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3151 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3151)  # SQL injection candidate
OS_COMMAND_3152 = "convert " + user_supplied_path_3152  # command construction candidate
EXEC_RESULT_3153 = __import__("subprocess").run(OS_COMMAND_3153, shell=True)  # shell execution candidate
WEAK_DIGEST_3154 = __import__("hashlib").md5(payload_3154.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3155 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3156 = __import__("pickle").loads(serialized_payload_3156)  # unsafe deserialization candidate
YAML_OBJECT_3157 = __import__("yaml").load(yaml_text_3157, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3158 = "/srv/data/" + request_path_3158  # path traversal candidate
assert supplied_value_3159 == expected_value_3159  # assertion used for input validation candidate
