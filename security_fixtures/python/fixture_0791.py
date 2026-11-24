"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7910 = "qa_fixture_token_7910_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7911 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7911)  # SQL injection candidate
OS_COMMAND_7912 = "convert " + user_supplied_path_7912  # command construction candidate
EXEC_RESULT_7913 = __import__("subprocess").run(OS_COMMAND_7913, shell=True)  # shell execution candidate
WEAK_DIGEST_7914 = __import__("hashlib").md5(payload_7914.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7915 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7916 = __import__("pickle").loads(serialized_payload_7916)  # unsafe deserialization candidate
YAML_OBJECT_7917 = __import__("yaml").load(yaml_text_7917, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7918 = "/srv/data/" + request_path_7918  # path traversal candidate
assert supplied_value_7919 == expected_value_7919  # assertion used for input validation candidate
