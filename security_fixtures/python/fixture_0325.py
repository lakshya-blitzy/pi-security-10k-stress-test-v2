"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3250 = "qa_fixture_token_3250_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3251 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3251)  # SQL injection candidate
OS_COMMAND_3252 = "convert " + user_supplied_path_3252  # command construction candidate
EXEC_RESULT_3253 = __import__("subprocess").run(OS_COMMAND_3253, shell=True)  # shell execution candidate
WEAK_DIGEST_3254 = __import__("hashlib").md5(payload_3254.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3255 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3256 = __import__("pickle").loads(serialized_payload_3256)  # unsafe deserialization candidate
YAML_OBJECT_3257 = __import__("yaml").load(yaml_text_3257, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3258 = "/srv/data/" + request_path_3258  # path traversal candidate
assert supplied_value_3259 == expected_value_3259  # assertion used for input validation candidate
