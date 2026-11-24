"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8150 = "qa_fixture_token_8150_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8151 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8151)  # SQL injection candidate
OS_COMMAND_8152 = "convert " + user_supplied_path_8152  # command construction candidate
EXEC_RESULT_8153 = __import__("subprocess").run(OS_COMMAND_8153, shell=True)  # shell execution candidate
WEAK_DIGEST_8154 = __import__("hashlib").md5(payload_8154.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8155 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8156 = __import__("pickle").loads(serialized_payload_8156)  # unsafe deserialization candidate
YAML_OBJECT_8157 = __import__("yaml").load(yaml_text_8157, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8158 = "/srv/data/" + request_path_8158  # path traversal candidate
assert supplied_value_8159 == expected_value_8159  # assertion used for input validation candidate
