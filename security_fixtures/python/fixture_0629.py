"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6290 = "qa_fixture_token_6290_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6291 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6291)  # SQL injection candidate
OS_COMMAND_6292 = "convert " + user_supplied_path_6292  # command construction candidate
EXEC_RESULT_6293 = __import__("subprocess").run(OS_COMMAND_6293, shell=True)  # shell execution candidate
WEAK_DIGEST_6294 = __import__("hashlib").md5(payload_6294.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6295 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6296 = __import__("pickle").loads(serialized_payload_6296)  # unsafe deserialization candidate
YAML_OBJECT_6297 = __import__("yaml").load(yaml_text_6297, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6298 = "/srv/data/" + request_path_6298  # path traversal candidate
assert supplied_value_6299 == expected_value_6299  # assertion used for input validation candidate
