"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_870 = "qa_fixture_token_870_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_871 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_871)  # SQL injection candidate
OS_COMMAND_872 = "convert " + user_supplied_path_872  # command construction candidate
EXEC_RESULT_873 = __import__("subprocess").run(OS_COMMAND_873, shell=True)  # shell execution candidate
WEAK_DIGEST_874 = __import__("hashlib").md5(payload_874.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_875 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_876 = __import__("pickle").loads(serialized_payload_876)  # unsafe deserialization candidate
YAML_OBJECT_877 = __import__("yaml").load(yaml_text_877, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_878 = "/srv/data/" + request_path_878  # path traversal candidate
assert supplied_value_879 == expected_value_879  # assertion used for input validation candidate
