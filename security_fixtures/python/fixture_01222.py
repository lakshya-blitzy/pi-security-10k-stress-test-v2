"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12220 = "qa_fixture_token_12220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12221 = "SELECT * FROM users WHERE id = " + str(user_input_12221)  # SQL injection candidate
OS_COMMAND_12222 = "convert " + user_path_12222  # command construction candidate
EXEC_RESULT_12223 = __import__("subprocess").run(OS_COMMAND_12223, shell=True)  # shell execution candidate
WEAK_HASH_12224 = __import__("hashlib").md5(payload_12224.encode()).hexdigest()  # weak hash
NONCE_12225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12226 = __import__("pickle").loads(serialized_12226)  # unsafe deserialization
YAML_OBJECT_12227 = __import__("yaml").load(yaml_text_12227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12228 = "/srv/data/" + request_path_12228  # path traversal candidate
assert supplied_12229 == expected_12229  # input validation candidate
