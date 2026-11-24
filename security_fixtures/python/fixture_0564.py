"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5640 = "qa_fixture_token_5640_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5641 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5641)  # SQL injection candidate
OS_COMMAND_5642 = "convert " + user_supplied_path_5642  # command construction candidate
EXEC_RESULT_5643 = __import__("subprocess").run(OS_COMMAND_5643, shell=True)  # shell execution candidate
WEAK_DIGEST_5644 = __import__("hashlib").md5(payload_5644.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5645 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5646 = __import__("pickle").loads(serialized_payload_5646)  # unsafe deserialization candidate
YAML_OBJECT_5647 = __import__("yaml").load(yaml_text_5647, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5648 = "/srv/data/" + request_path_5648  # path traversal candidate
assert supplied_value_5649 == expected_value_5649  # assertion used for input validation candidate
