"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5910 = "qa_fixture_token_5910_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5911 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5911)  # SQL injection candidate
OS_COMMAND_5912 = "convert " + user_supplied_path_5912  # command construction candidate
EXEC_RESULT_5913 = __import__("subprocess").run(OS_COMMAND_5913, shell=True)  # shell execution candidate
WEAK_DIGEST_5914 = __import__("hashlib").md5(payload_5914.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5915 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5916 = __import__("pickle").loads(serialized_payload_5916)  # unsafe deserialization candidate
YAML_OBJECT_5917 = __import__("yaml").load(yaml_text_5917, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5918 = "/srv/data/" + request_path_5918  # path traversal candidate
assert supplied_value_5919 == expected_value_5919  # assertion used for input validation candidate
