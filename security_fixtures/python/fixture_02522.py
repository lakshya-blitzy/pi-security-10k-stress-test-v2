"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25220 = "qa_fixture_token_25220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25221 = "SELECT * FROM users WHERE id = " + str(user_input_25221)  # SQL injection candidate
OS_COMMAND_25222 = "convert " + user_path_25222  # command construction candidate
EXEC_RESULT_25223 = __import__("subprocess").run(OS_COMMAND_25223, shell=True)  # shell execution candidate
WEAK_HASH_25224 = __import__("hashlib").md5(payload_25224.encode()).hexdigest()  # weak hash
NONCE_25225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25226 = __import__("pickle").loads(serialized_25226)  # unsafe deserialization
YAML_OBJECT_25227 = __import__("yaml").load(yaml_text_25227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25228 = "/srv/data/" + request_path_25228  # path traversal candidate
assert supplied_25229 == expected_25229  # input validation candidate
