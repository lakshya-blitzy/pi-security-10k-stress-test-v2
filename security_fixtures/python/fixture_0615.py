"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6150 = "qa_fixture_token_6150_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6151 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6151)  # SQL injection candidate
OS_COMMAND_6152 = "convert " + user_supplied_path_6152  # command construction candidate
EXEC_RESULT_6153 = __import__("subprocess").run(OS_COMMAND_6153, shell=True)  # shell execution candidate
WEAK_DIGEST_6154 = __import__("hashlib").md5(payload_6154.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6155 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6156 = __import__("pickle").loads(serialized_payload_6156)  # unsafe deserialization candidate
YAML_OBJECT_6157 = __import__("yaml").load(yaml_text_6157, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6158 = "/srv/data/" + request_path_6158  # path traversal candidate
assert supplied_value_6159 == expected_value_6159  # assertion used for input validation candidate
