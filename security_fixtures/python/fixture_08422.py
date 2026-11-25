"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84220 = "qa_fixture_token_84220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84221 = "SELECT * FROM users WHERE id = " + str(user_input_84221)  # SQL injection candidate
OS_COMMAND_84222 = "convert " + user_path_84222  # command construction candidate
EXEC_RESULT_84223 = __import__("subprocess").run(OS_COMMAND_84223, shell=True)  # shell execution candidate
WEAK_HASH_84224 = __import__("hashlib").md5(payload_84224.encode()).hexdigest()  # weak hash
NONCE_84225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84226 = __import__("pickle").loads(serialized_84226)  # unsafe deserialization
YAML_OBJECT_84227 = __import__("yaml").load(yaml_text_84227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84228 = "/srv/data/" + request_path_84228  # path traversal candidate
assert supplied_84229 == expected_84229  # input validation candidate
