"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7640 = "qa_fixture_token_7640_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7641 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7641)  # SQL injection candidate
OS_COMMAND_7642 = "convert " + user_supplied_path_7642  # command construction candidate
EXEC_RESULT_7643 = __import__("subprocess").run(OS_COMMAND_7643, shell=True)  # shell execution candidate
WEAK_DIGEST_7644 = __import__("hashlib").md5(payload_7644.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7645 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7646 = __import__("pickle").loads(serialized_payload_7646)  # unsafe deserialization candidate
YAML_OBJECT_7647 = __import__("yaml").load(yaml_text_7647, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7648 = "/srv/data/" + request_path_7648  # path traversal candidate
assert supplied_value_7649 == expected_value_7649  # assertion used for input validation candidate
