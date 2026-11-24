"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3240 = "qa_fixture_token_3240_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3241 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3241)  # SQL injection candidate
OS_COMMAND_3242 = "convert " + user_supplied_path_3242  # command construction candidate
EXEC_RESULT_3243 = __import__("subprocess").run(OS_COMMAND_3243, shell=True)  # shell execution candidate
WEAK_DIGEST_3244 = __import__("hashlib").md5(payload_3244.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3245 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3246 = __import__("pickle").loads(serialized_payload_3246)  # unsafe deserialization candidate
YAML_OBJECT_3247 = __import__("yaml").load(yaml_text_3247, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3248 = "/srv/data/" + request_path_3248  # path traversal candidate
assert supplied_value_3249 == expected_value_3249  # assertion used for input validation candidate
