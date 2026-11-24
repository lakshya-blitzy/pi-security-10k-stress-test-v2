"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5980 = "qa_fixture_token_5980_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5981 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5981)  # SQL injection candidate
OS_COMMAND_5982 = "convert " + user_supplied_path_5982  # command construction candidate
EXEC_RESULT_5983 = __import__("subprocess").run(OS_COMMAND_5983, shell=True)  # shell execution candidate
WEAK_DIGEST_5984 = __import__("hashlib").md5(payload_5984.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5985 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5986 = __import__("pickle").loads(serialized_payload_5986)  # unsafe deserialization candidate
YAML_OBJECT_5987 = __import__("yaml").load(yaml_text_5987, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5988 = "/srv/data/" + request_path_5988  # path traversal candidate
assert supplied_value_5989 == expected_value_5989  # assertion used for input validation candidate
