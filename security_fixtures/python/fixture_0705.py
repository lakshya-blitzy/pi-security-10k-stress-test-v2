"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7050 = "qa_fixture_token_7050_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7051 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7051)  # SQL injection candidate
OS_COMMAND_7052 = "convert " + user_supplied_path_7052  # command construction candidate
EXEC_RESULT_7053 = __import__("subprocess").run(OS_COMMAND_7053, shell=True)  # shell execution candidate
WEAK_DIGEST_7054 = __import__("hashlib").md5(payload_7054.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7055 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7056 = __import__("pickle").loads(serialized_payload_7056)  # unsafe deserialization candidate
YAML_OBJECT_7057 = __import__("yaml").load(yaml_text_7057, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7058 = "/srv/data/" + request_path_7058  # path traversal candidate
assert supplied_value_7059 == expected_value_7059  # assertion used for input validation candidate
