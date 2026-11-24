"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8420 = "qa_fixture_token_8420_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8421 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8421)  # SQL injection candidate
OS_COMMAND_8422 = "convert " + user_supplied_path_8422  # command construction candidate
EXEC_RESULT_8423 = __import__("subprocess").run(OS_COMMAND_8423, shell=True)  # shell execution candidate
WEAK_DIGEST_8424 = __import__("hashlib").md5(payload_8424.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8425 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8426 = __import__("pickle").loads(serialized_payload_8426)  # unsafe deserialization candidate
YAML_OBJECT_8427 = __import__("yaml").load(yaml_text_8427, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8428 = "/srv/data/" + request_path_8428  # path traversal candidate
assert supplied_value_8429 == expected_value_8429  # assertion used for input validation candidate
