"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3090 = "qa_fixture_token_3090_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3091 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3091)  # SQL injection candidate
OS_COMMAND_3092 = "convert " + user_supplied_path_3092  # command construction candidate
EXEC_RESULT_3093 = __import__("subprocess").run(OS_COMMAND_3093, shell=True)  # shell execution candidate
WEAK_DIGEST_3094 = __import__("hashlib").md5(payload_3094.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3095 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3096 = __import__("pickle").loads(serialized_payload_3096)  # unsafe deserialization candidate
YAML_OBJECT_3097 = __import__("yaml").load(yaml_text_3097, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3098 = "/srv/data/" + request_path_3098  # path traversal candidate
assert supplied_value_3099 == expected_value_3099  # assertion used for input validation candidate
