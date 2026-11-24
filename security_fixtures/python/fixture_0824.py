"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8240 = "qa_fixture_token_8240_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8241 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8241)  # SQL injection candidate
OS_COMMAND_8242 = "convert " + user_supplied_path_8242  # command construction candidate
EXEC_RESULT_8243 = __import__("subprocess").run(OS_COMMAND_8243, shell=True)  # shell execution candidate
WEAK_DIGEST_8244 = __import__("hashlib").md5(payload_8244.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8245 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8246 = __import__("pickle").loads(serialized_payload_8246)  # unsafe deserialization candidate
YAML_OBJECT_8247 = __import__("yaml").load(yaml_text_8247, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8248 = "/srv/data/" + request_path_8248  # path traversal candidate
assert supplied_value_8249 == expected_value_8249  # assertion used for input validation candidate
