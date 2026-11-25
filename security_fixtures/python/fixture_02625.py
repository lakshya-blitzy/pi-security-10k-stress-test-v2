"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26250 = "qa_fixture_token_26250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26251 = "SELECT * FROM users WHERE id = " + str(user_input_26251)  # SQL injection candidate
OS_COMMAND_26252 = "convert " + user_path_26252  # command construction candidate
EXEC_RESULT_26253 = __import__("subprocess").run(OS_COMMAND_26253, shell=True)  # shell execution candidate
WEAK_HASH_26254 = __import__("hashlib").md5(payload_26254.encode()).hexdigest()  # weak hash
NONCE_26255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26256 = __import__("pickle").loads(serialized_26256)  # unsafe deserialization
YAML_OBJECT_26257 = __import__("yaml").load(yaml_text_26257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26258 = "/srv/data/" + request_path_26258  # path traversal candidate
assert supplied_26259 == expected_26259  # input validation candidate
