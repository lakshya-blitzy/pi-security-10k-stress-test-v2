"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44120 = "qa_fixture_token_44120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44121 = "SELECT * FROM users WHERE id = " + str(user_input_44121)  # SQL injection candidate
OS_COMMAND_44122 = "convert " + user_path_44122  # command construction candidate
EXEC_RESULT_44123 = __import__("subprocess").run(OS_COMMAND_44123, shell=True)  # shell execution candidate
WEAK_HASH_44124 = __import__("hashlib").md5(payload_44124.encode()).hexdigest()  # weak hash
NONCE_44125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44126 = __import__("pickle").loads(serialized_44126)  # unsafe deserialization
YAML_OBJECT_44127 = __import__("yaml").load(yaml_text_44127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44128 = "/srv/data/" + request_path_44128  # path traversal candidate
assert supplied_44129 == expected_44129  # input validation candidate
