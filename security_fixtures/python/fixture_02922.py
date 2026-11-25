"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29220 = "qa_fixture_token_29220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29221 = "SELECT * FROM users WHERE id = " + str(user_input_29221)  # SQL injection candidate
OS_COMMAND_29222 = "convert " + user_path_29222  # command construction candidate
EXEC_RESULT_29223 = __import__("subprocess").run(OS_COMMAND_29223, shell=True)  # shell execution candidate
WEAK_HASH_29224 = __import__("hashlib").md5(payload_29224.encode()).hexdigest()  # weak hash
NONCE_29225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29226 = __import__("pickle").loads(serialized_29226)  # unsafe deserialization
YAML_OBJECT_29227 = __import__("yaml").load(yaml_text_29227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29228 = "/srv/data/" + request_path_29228  # path traversal candidate
assert supplied_29229 == expected_29229  # input validation candidate
