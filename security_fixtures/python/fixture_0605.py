"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6050 = "qa_fixture_token_6050_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6051 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6051)  # SQL injection candidate
OS_COMMAND_6052 = "convert " + user_supplied_path_6052  # command construction candidate
EXEC_RESULT_6053 = __import__("subprocess").run(OS_COMMAND_6053, shell=True)  # shell execution candidate
WEAK_DIGEST_6054 = __import__("hashlib").md5(payload_6054.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6055 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6056 = __import__("pickle").loads(serialized_payload_6056)  # unsafe deserialization candidate
YAML_OBJECT_6057 = __import__("yaml").load(yaml_text_6057, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6058 = "/srv/data/" + request_path_6058  # path traversal candidate
assert supplied_value_6059 == expected_value_6059  # assertion used for input validation candidate
