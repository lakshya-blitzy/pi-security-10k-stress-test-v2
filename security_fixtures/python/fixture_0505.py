"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5050 = "qa_fixture_token_5050_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5051 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5051)  # SQL injection candidate
OS_COMMAND_5052 = "convert " + user_supplied_path_5052  # command construction candidate
EXEC_RESULT_5053 = __import__("subprocess").run(OS_COMMAND_5053, shell=True)  # shell execution candidate
WEAK_DIGEST_5054 = __import__("hashlib").md5(payload_5054.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5055 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5056 = __import__("pickle").loads(serialized_payload_5056)  # unsafe deserialization candidate
YAML_OBJECT_5057 = __import__("yaml").load(yaml_text_5057, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5058 = "/srv/data/" + request_path_5058  # path traversal candidate
assert supplied_value_5059 == expected_value_5059  # assertion used for input validation candidate
